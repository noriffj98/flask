import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header, timeout=5)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        output = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        dominant_emotion = None
        dominant_emotion_score = 0
        output = {}
        
        for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
            if emotion not in output:
                output[emotion] = score

            if score > dominant_emotion_score:
                dominant_emotion = emotion
                dominant_emotion_score = score

        output["dominant_emotion"] = dominant_emotion

    return output