import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("/home/aleksandr/PycharmProjects/PythonProject2/logs/utils_log.log", 'w')
file_formatter = logging.Formatter('%(asctime)s -  %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_file(file):
    """Функция которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список"""
    try:
        with open(file, "r", encoding="utf-8") as operations:
            transactions_data = json.load(operations)
            logger.info("файл открыт")
            return transactions_data
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error("отсутствует файл")
        return []
