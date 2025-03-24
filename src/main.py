import re

from src.bank_operation import search_operation
from src.fin_tranzaction import csv_file, xlsx_file
from src.processing import sort_by_date
from src.utils import json_file
from src.widget import get_date, mask_account_card


def currency_file(transactions, input_currency="RUB"):
    """функция для фильтрации валюты json, csv и xlsx файлов"""
    currency = []
    for key in transactions:
        if "operationAmount" in key:
            if key["operationAmount"]["currency"]["code"] == input_currency:
                currency.append(key)
        elif "currency_name" in key:
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
                currency_ = currency_file(sort_by_yes_false)
                if by_word == "да":
                    keyword = input("Введите слово для фильтрации")
                    filtered_word = filter_by_word(currency_, keyword)
                    return filtered_word
                return currency_
            elif currency_transactions == "нет":
                if by_word == "да":
                    keyword = input("Введите слово для фильтрации")
                    not_ruble_word = filter_by_word(sort_by_yes_false, keyword)
                    return not_ruble_word
            return sort_by_yes_false
        elif sorted_bool == "по возрастанию":
            if currency_transactions == "да":
                sorting_ruble = currency_file(sort_by_yes)
                if by_word == "да":
                    keyword = input("Введите слово для фильтрации")
                    filtration_ruble = filter_by_word(sorting_ruble, keyword)
                    return filtration_ruble
                return sorting_ruble
            elif currency_transactions == "нет":
                if by_word == "да":
                    keyword = input("Введите слово для фильтрации")
                    filtration_no_ruble = filter_by_word(sort_by_yes, keyword)
                    return filtration_no_ruble
            return sort_by_yes
    elif  sorted_operation == "нет":
        currency_transactions = input("Выводить только рублевые тразакции? Да/Нет").lower()
        by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
        if currency_transactions == "да":
            no_filtration_ruble = currency_file(filter_by_status)
            if by_word == "да":
                keyword = input("Введите слово для фильтрации")
                ruble_and_filtration = filter_by_word(no_filtration_ruble, keyword)
                return ruble_and_filtration
            return no_filtration_ruble
        elif currency_transactions == "нет":
            if by_word == "да":
                keyword = input("Введите слово для фильтрации")
                no_ruble_filtration = filter_by_word(filter_by_status, keyword)
                return no_ruble_filtration
        return filter_by_status


function = main()

print("Распечатываю итоговый список транзакций...")
if not function:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
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
