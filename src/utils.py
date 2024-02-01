import requests
from _datetime import datetime


def get_json(user_val):
    name = "https://www.cbr-xml-daily.ru/daily_json.js"
    dict_currency = {}

    current_time = datetime.today()
    currencies = requests.get(name).json()["Valute"]
    current_currency = currencies[user_val]
    dict_currency["current_time"] = datetime.strftime(current_time, "%d.%m.%Y %H:%M:%S")
    dict_currency["name_curr"] = current_currency["Name"]
    dict_currency["value_curr"] = current_currency["Value"]

    return dict_currency
