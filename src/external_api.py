import os

import requests
from dotenv import load_dotenv

from src.utils import json_file

load_dotenv()

API_KEY = os.getenv("API_KEY")
file = json_file("/home/aleksandr/PycharmProjects/PythonProject2/data/operations.json")


def convert_in_rub(transaction):
    """Принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях, тип данных —float. Если транзакция была в USD
    или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли"""
    headers = {"apikey": "API_KEY"}
    amount = transaction['operationAmount']['amount']
    code = transaction['operationAmount']['currency']['code']
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers)
    return response.json()


for i in file:
    if i.get("operationAmount"):
        amon = convert_in_rub(i)
        print(amon)
