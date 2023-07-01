import ai21
import prompts
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
        except json.decoder.JSONDecodeError as e:
            pass
    return data


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


def profession(user_input):
    data = api_request(prompt=prompts.profession_prompt.format(input=user_input),
                       maxTokens=60,
                       temperature=0.65,
                       stopSequences=["##"])
    data = data['suggested_professions']
    print(data)

    return data
