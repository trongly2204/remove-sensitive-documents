from flask import Flask, request, jsonify
from regex_detector import regex_method
from ner_detector import ner_method

app = Flask(__name__)

# API Route
@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    text = data.get("text", "")

    sanitizer_text = regex_method(text)

    sanitizer_text = ner_method(sanitizer_text)

    response = {"original_text": text, "redacted_text": sanitizer_text}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
