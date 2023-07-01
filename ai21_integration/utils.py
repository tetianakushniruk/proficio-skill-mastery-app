import ai21
import prompts
import json

import os
from dotenv import load_dotenv

load_dotenv()
ai21.api_key = os.getenv('API_KEY')

def roadmap(field):
    response = ai21.Completion.execute(
        model="j2-mid",
        prompt=prompts.roadmap_prompt.format(field=field),
        numResults=1,
        maxTokens=570,
        temperature=0.61,
        topKReturn=0,
        topP=1,
        countPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        frequencyPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        presencePenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        stopSequences=["##"]
    )

    data = response['completions'][0]['data']['text']
    data = json.loads(data)['roadmap']

    for i, d in enumerate(data):
        name = d['name']
        desc = d['description']
        print(f'{i + 1}. {name}: {desc}')

    return data

