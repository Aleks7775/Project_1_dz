import re

from src.bank_operation import search_operation
from src.fin_tranzaction import csv_file, xlsx_file
from src.processing import sort_by_date
from src.utils import json_file
from src.widget import get_date, mask_account_card


def currency_js(transactions, input_currency):
    """функция для фильтрации валюты json файлов"""
    currency = []
    for key in transactions:
        if key.get('operationAmount'):
            if key["operationAmount"]["currency"]["code"] == input_currency:
                currency.append(key)
    return currency


def currency_csv_xlsx(transactions, input_currency):
    """функция для фильтрации валюты csv и xlsx файлов"""
    currency = []
    for key in transactions:
        if key["currency_code"] == input_currency:
            currency.append(key)
    return currency


def filter_by_word(list_dict, string):
    """Функция для поиска транзакций по заданной строке"""
    pattern = re.compile(string, flags=re.IGNORECASE)
    filter_transactions = []
    for key in list_dict:
        if 'description' in key and isinstance(key['description'], str) and pattern.search(key['description']):
            filter_transactions.append(key)
    return filter_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")

    user = input()
    if user == '1':
        transaction = json_file("/home/aleksandr/PycharmProjects/PythonProject2/data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif user == '2':
        transaction = csv_file("/home/aleksandr/PycharmProjects/PythonProject2/data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif user == '3':
        transaction = xlsx_file("/home/aleksandr/PycharmProjects/PythonProject2/data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")

    print("Введите статус, по которому необходимо выполнить фильтрацию.\n"      
    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    while True:
        status = input()
        if status.upper() in ("EXECUTED", "CANCELED", "PENDING"):
            break
        print(f'Статус операции "{status}" недоступен')
    print(f'Операции отфильтрованы по статусу "{status.upper()}"')

    filter_by_status = search_operation(transaction, status.upper())
    sorted_operation = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sorted_operation == "да":
        sort_by_yes = sort_by_date(filter_by_status)
        sort_by_yes_false = sort_by_date(filter_by_status, False)
        sorted_bool = input("Отсортировать по возрастанию или по убыванию?")
        currency_transactions = input("Выводить только рублевые тразакции? Да/Нет").lower()
        by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
        if sorted_bool == "по убыванию":
            if currency_transactions == "да":
                    if user == "1":
                        operation_js = currency_js(sort_by_yes_false, "RUB")
                        if by_word == "да":
                            keyword = input("Введите слово для фильтрации")
                            return filter_by_word(operation_js, keyword)
                        return  operation_js
                    elif user in ("2", "3"):
                        operation_cs_xl = currency_csv_xlsx(sort_by_yes_false, "RUB")
                        if by_word == "да":
                            keyword = input("Введите слово для фильтрации")
                            return filter_by_word(operation_cs_xl, keyword)
                        return operation_cs_xl
            return sort_by_yes_false
        elif "по возрастанию":
            if currency_transactions == "да":
                    if user == "1":
                        operation_js_age = currency_js(sort_by_yes, "RUB")
                        if by_word == "да":
                            keyword = input("Введите слово для фильтрации")
                            return filter_by_word(operation_js_age, keyword)
                        return operation_js_age
                    elif user in ("2", "3"):
                        operation_cs_age = currency_csv_xlsx(sort_by_yes, "RUB")
                        if by_word == "да":
                            keyword = input("Введите слово для фильтрации")
                            return filter_by_word(operation_cs_age, keyword)
                        return operation_cs_age
            return sort_by_yes


function = main()

print(f"\nВсего банковских операций в выборке: {len(function)}\n")
for i in function:
    if isinstance(i["date"], str) and (len(i["date"]) == 20 or len(i["date"]) == 26):
        data = get_date(i["date"])
        check = mask_account_card(i["to"])
        if "operationAmount" in i:
            if i["description"] == "Открытие вклада":
                print(f"{data} {i["description"]}")
                print(check)
                print(f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}")
                print()
            else:
                print(f"{data} {i["description"]}")
                print(f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}")
                print(f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}")
                print()
        else:
            if i["description"] == "Открытие вклада":
                print(f"{data} {i["description"]}")
                print(check)
                print(f"Сумма: {int(i["amount"])} {i["currency_name"]}.")
                print()
            else:
                print(f"{data} {i["description"]}")
                print(f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}")
                print(f"Сумма: {int(i["amount"])} {i["currency_name"]}.")
                print()
