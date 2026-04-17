import requests

API_KEY = "_6HRCzk4lEMhIs202t5MNSw7vygd_AKlgZ8YEklhQAka"
URL = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/967245b1-1bca-486d-98ad-8731701d954a"


def detect_emotion(text):
    endpoint = f"{URL}/v1/analyze?version=2022-04-07"

    try:
        response = requests.post(
            endpoint,
            auth=("apikey", API_KEY),
            headers={"Content-Type": "application/json"},
            json={
                "text": text,
                "features": {"emotion": {}}
            },
            timeout=10
        )

        data = response.json()

        return data.get("emotion", {}).get("document", {}).get("emotion", {})

    except Exception as e:
        return {"error": str(e)}
