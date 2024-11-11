"""
This module provides a function to analyze sentiment using a Watson NLP API.
"""

import json # Import the json library to format text into dictionary
import requests # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):
    '''Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    '''
    url = '''https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'''
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header, timeout=5)  # Set timeout to 5 seconds
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None
    return {"label": label, "score": score}
