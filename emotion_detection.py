from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ===== IBM Watson NLU Credentials =====
API_KEY = "xxx"
URL = "xxx"


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

        # If API error
        if response.status_code != 200:
            return {"error": data}

        # Extract emotions safely
        emotions = (
            data.get("emotion", {})
                .get("document", {})
                .get("emotion", {})
        )

        if not emotions:
            return {"error": "No emotion detected. Try a longer sentence."}

        return emotions

    except Exception as e:
        return {"error": str(e)}


@app.route("/", methods=["GET", "POST"])
def index():
    emotions = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        emotions = get_emotion(text)

    return render_template("index.html", emotions=emotions, text=text)


if __name__ == "__main__":
    app.run(debug=True)
