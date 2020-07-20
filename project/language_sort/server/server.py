import json

from flask import Flask, request

from language_sort.sorter.api.api import API

app = Flask(__name__)


@app.route('/', methods=["POST"])
def get_language():
    data = request.json

    if "text" not in data:
        return "text should be in keys", 400
    text = data.get("text")
    if not isinstance(text, str):
        return "text must be string", 400
    api = API()
    api.pull_languages(text)
    lang = api.get_language(text)
    response = {"lang": lang}
    response_string = json.dumps(response)
    return response_string


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
