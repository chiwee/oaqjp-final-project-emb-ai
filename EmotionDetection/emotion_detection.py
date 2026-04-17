import requests

API_KEY = "xxx"
URL = "xxx"


def emotion_detector(text_to_analyse):

    # Handle empty input
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Correct Watson NLP endpoint (REQUIRED by Coursera)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Required header (STRICT MATCH)
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Required payload format
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # POST request
    response = requests.post(url, json=payload, headers=headers)

    # Handle bad request
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Parse response safely
    data = response.json()

    emotions = data["emotionPredictions"][0]["emotion"]

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Add required key
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
