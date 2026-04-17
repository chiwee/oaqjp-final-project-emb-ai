from flask import Blueprint, render_template, request, jsonify
from .watson_service import detect_emotion

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    text = data.get("text", "")

    result = detect_emotion(text)

    return jsonify(result)
