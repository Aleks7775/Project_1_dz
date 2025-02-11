from typing import Dict, List


def filter_by_state(list_dict: List[Dict], value_key: str = 'EXECUTED') -> List[Dict]:
    """функция которая принимает список словарей и опционально значение для ключа
(state) и возвращает новый список словарей, содержащий только те словари, у которых ключ
(state) соответствует указанному значению"""
    new_list = []
    for dictionary in list_dict:
        if dictionary['state'] == value_key:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_dict: List[Dict], sort_key: bool = True) -> List[Dict]:
    """функция которая принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict['date'], reverse=not sort_key)
    return sort_list


"""Проверка функций"""
my_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(my_list))
print(sort_by_date(my_list))
