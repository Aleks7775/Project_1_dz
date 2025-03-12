from typing import Dict, List, Union


def filter_by_state(list_dict: List[Dict], value_key: str = 'EXECUTED') -> Union[List[Dict], str]:
    """функция, которая принимает список словарей и опционально значение для ключа
(state) и возвращает новый список словарей, содержащий только те словари, у которых ключ
(state) соответствует указанному значению"""
    new_list = []
    for dictionary in list_dict:
        if 'state' not in dictionary:
            return "Отсутствует ключ state"
        if dictionary['state'] == value_key:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_dict: List[Dict], sort_key: bool = True) -> List[Dict]:
    """функция, которая принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict['date'], reverse=not sort_key)
    return sort_list
