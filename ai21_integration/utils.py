import ai21
import requests

from ai21_integration import prompts
import json

import os
from dotenv import load_dotenv

load_dotenv()
ai21.api_key = os.getenv('API_KEY')

def api_request(**kwargs):
    default_params = {
        'model': "j2-mid",
        'prompt': "",
        'numResults': 1,
        'maxTokens': 200,
        'temperature': 0.7,
        'topKReturn': 0,
        'topP': 1,
        'countPenalty': {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        'frequencyPenalty': {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        'presencePenalty': {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        'stopSequences': []
    }

    params = {**default_params, **kwargs}
    while True:
        response = ai21.Completion.execute(**params)
        data = response['completions'][0]['data']['text']
        try:
            data = json.loads(data)
            break
        except json.decoder.JSONDecodeError:
            pass
    return data


def is_valid_profession(field):
    data = api_request(model="j2-ultra",
                       prompt=prompts.valid_profession_prompt.format(field=field),
                       maxTokens=35,
                       temperature=0.8,
                       stopSequences=["##"])
    if data['valid'].lower() == 'true':
        return True, None
    elif data['valid'].lower() == 'false':
        return False, data['message']
    else:
        return False, None

def roadmap(field):
    data = api_request(prompt=prompts.roadmap_prompt.format(field=field),
                       maxTokens=570,
                       temperature=0.61,
                       stopSequences=["##"])
    data = data['roadmap']

    for i, d in enumerate(data):
        name = d['name']
        desc = d['description']
        print(f'{i + 1}. {name}: {desc}')

    return data

def book_cover(name, author):
    search_base_url = 'https://openlibrary.org/search.json'
    cover_base_url = 'https://covers.openlibrary.org/b/olid/{olid}-L.jpg'
    params = {
        'q': ' '.join([name, author]),
        'mode': 'everything',
        'language': 'eng'
    }
    response = requests.get(search_base_url, params=params)
    try:
        response.raise_for_status()
        data = response.json()
    except (requests.HTTPError, ValueError) as e:
        return None

    ids_list = []
    if not data['num_found']:
        return None

    for book in data['docs']:
        if 'cover_edition_key' in book.keys():
            ids_list.append((book['cover_edition_key'],
                            max(book['publish_year'])))
    if not ids_list:
        return None

    ids_list.sort(key=lambda x: x[1], reverse=True)
    cover_url = cover_base_url.format(olid=ids_list[0][0])

    return cover_url

def books(field):
    data = api_request(prompt=prompts.books_prompt.format(field=field),
                       maxTokens=450,
                       temperature=0.75,
                       stopSequences=["##"])
    data = data['books']

    for i, d in enumerate(data):
        name = d['name']
        author = d['author']
        desc = d['description']
        data[i]['cover_url'] = book_cover(name, author)
        print(f'{i + 1}. "{name}" by {author}: {desc}')

    return data


def interview_q(field):
    data = api_request(prompt=prompts.interview_q_prompt.format(field=field),
                       maxTokens=450,
                       temperature=0.7,
                       stopSequences=["##"])
    data = data['interview_questions']

    for i, d in enumerate(data):
        question = d['question']
        answer = d['answer']
        print(f'{i + 1}. {question}: {answer}')

    return data


def tip(field):
    data = api_request(prompt=prompts.tip_prompt.format(field=field),
                       maxTokens=190,
                       temperature=0.85,
                       stopSequences=["##"])
    data = data['tip']
    print(data)

    return data


def professions(user_input):
    data = api_request(prompt=prompts.profession_prompt.format(input=user_input),
                       maxTokens=60,
                       temperature=0.65,
                       stopSequences=["##"])
    data = data['suggested_professions']
    print(data)

    if not isinstance(data, list):
        raise TypeError

    return data
