from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# ====== IBM Watson NLU Credentials ======
API_KEY = "Y6rJkSTpc4uQuAjxat5oE-Pn2JOtzwZItZFqZgHDPmdX"
URL = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/967245b1-1bca-486d-98ad-8731701d954a"  # e.g. https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/xxx

def get_emotion(text):
    endpoint = f"{URL}/v1/analyze?version=2022-04-07"

    headers = {
        "Content-Type": "application/json"
    }

    auth = ("apikey", API_KEY)

    data = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(endpoint, headers=headers, auth=auth, json=data)
    
    if response.status_code != 200:
        return {"error": response.text}

    result = response.json()

    emotions = result["emotion"]["document"]["emotion"]
    return emotions


@app.route("/", methods=["GET", "POST"])
def index():
    emotions = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form["text"]
        emotions = get_emotion(user_text)

    return render_template("index.html", emotions=emotions, text=user_text)


if __name__ == "__main__":
    app.run(debug=True)
