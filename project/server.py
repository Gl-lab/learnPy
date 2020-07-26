import json

from flask import Flask, request

from api import API

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_language():
    data = request.json
    if data == None:
        return "Параметры не найдены", 400
    if "date" not in data:
        return "Дата не найдена", 400
    
    date = data.get("date")
    if not isinstance(date, str):
        return "date must be string YYYY-mm-dd", 400
    
    dateParam = datetime.datetime.strptime(date, "%Y-%m-%d")
    api = API()
    cases = api.get_cases_by_date(date)
    response = {"cases": cases}
    response_string = json.dumps(response)
    return response_string


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
