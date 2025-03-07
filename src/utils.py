import json


def json_file(file):
    """Функция которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список"""
    try:
        with open(file, "r", encoding="utf-8") as operations:
            transactions_data = json.load(operations)
            return transactions_data
    except (json.JSONDecodeError, FileNotFoundError):
        return []
