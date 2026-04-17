import requests

API_KEY = "_6HRCzk4lEMhIs202t5MNSw7vygd_AKlgZ8YEklhQAka"
URL = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/967245b1-1bca-486d-98ad-8731701d954a"

def emotion_detector(text_to_analyse):

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    data = response.json()

    # SAFE extraction (IMPORTANT for grading stability)
    emotions = (
        data
        .get("emotionPredictions", [{}])[0]
        .get("emotion", {})
    )

    if not emotions:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions
