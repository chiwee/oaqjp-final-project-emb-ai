from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()

    text = data.get("text", "")

    result = emotion_detector(text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
