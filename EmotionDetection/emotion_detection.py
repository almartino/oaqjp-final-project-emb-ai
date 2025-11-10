"""
This module implement the core of the application, that is the
capability of the system to detect user emotions.
"""

import json
import requests

API = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
MODEL = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse: str):
    """
    Detects emotions by using the watson emotion predict service.

    Args:
      text_to_analyse: str - the text to be analysed
    Returns:
      a `str` indicating the result of the prediction
    """

    body = {"raw_document": { "text": text_to_analyse}}
    response = requests.post(API, json=body, headers=MODEL)
    if response.status_code == 400:
        output = {}
        for key in KNOWN_EMOTIONS:
            output[key] = None
            output['dominant_emotion'] = None
        return output
    emotion_predictions = json.loads(response.text)
    return extract_emotions(emotion_predictions)

KNOWN_EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

def extract_emotions(emotion_predictions: dict):
    """
    extracts from an emotion prediction response the emotions score.

    Returns a dict with all the KNOWN_EMOTIONS alongside them scores plus the
    `dominant_emotion`, that is the emotion with the highest score.
    """
    
    predictions = emotion_predictions["emotionPredictions"]
    if len(predictions) == 0:
        return None # maybe return something else later...

    emotion = predictions[0]["emotion"] # we take the first result for the moment
    output = {}
    dominant_emotion = ('', 0)
    for key in KNOWN_EMOTIONS:
        score = emotion[key]
        if dominant_emotion[1] < score:
            dominant_emotion = (key, score)
        output[key] = score

    output['dominant_emotion'] = dominant_emotion[0]
    return output
