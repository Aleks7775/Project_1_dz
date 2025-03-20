import re
from collections import Counter

from src.fin_tranzaction import csv_file, xlsx_file
from src.utils import json_file

transactions = json_file("/home/aleksandr/PycharmProjects/PythonProject2/data/operations.json")
tr = csv_file("/home/aleksandr/PycharmProjects/PythonProject2/data/transactions.csv")
xr = xlsx_file("/home/aleksandr/PycharmProjects/PythonProject2/data/transactions_excel.xlsx")


def search_operation(list_dict, string):
    """Функция для поиска транзакций по заданной строке"""
    pattern = re.compile(string, flags=re.IGNORECASE)
    filter_transactions = []
    for i in list_dict:
        if 'state' in i and isinstance(i['state'], str) and pattern.search(i['state']):
            filter_transactions.append(i)
    return filter_transactions


def category_operations(list_dict, description=[]):
    """ Функция принимает список транзакций и список категорий, а возвращает словарь
    с количеством операций в каждой категории."""
    operation = [transaction['description'] for transaction in list_dict]
    cnt = Counter(operation)
    result = {}
    for i in description:
        result[i] = cnt[i]
    return result
