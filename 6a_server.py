from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# =========================
# IBM Watson NLU Config
# =========================
API_KEY = "_6HRCzk4lEMhIs202t5MNSw7vygd_AKlgZ8YEklhQAka"
URL = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/967245b1-1bca-486d-98ad-8731701d954a"


# =========================
# Emotion Detection Function
# =========================
def get_emotion(text):
    endpoint = f"{URL}/v1/analyze?version=2022-04-07"

    payload = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    try:
        response = requests.post(
            endpoint,
            auth=("apikey", API_KEY),
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=10
        )

        data = response.json()

        # Handle API error
        if response.status_code != 200:
            return {
                "error": data.get("error", "Watson API error"),
                "details": data
            }

        emotions = (
            data.get("emotion", {})
                .get("document", {})
                .get("emotion", {})
        )

        if not emotions:
            return {"error": "No emotion detected"}

        return emotions

    except Exception as e:
        return {"error": str(e)}


# =========================
# Routes
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No input text provided"}), 400

    text = data["text"]
    result = get_emotion(text)

    return jsonify(result)


# =========================
# Run Server
# =========================
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
