from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_prod: Union[str]) -> str:
    """Функция маскировки номера и счета в банке"""
    if isinstance(bank_prod, str):
        bank_prod_split = bank_prod.split(" ")
        num_prod = bank_prod_split[-1]
        name_prod = bank_prod_split[:-1]
        if "Счет" in bank_prod:
            if len(num_prod) == 20:
                return f"{"".join(name_prod)} {get_mask_account(num_prod)}"
        if len(num_prod) == 16:
            return f"{" ".join(name_prod)} {get_mask_card_number(num_prod)}"
    return "некорректный номер карты или счета"


def get_date(data: Union[str]) -> str:
    """Функция которая принимает на вход строку с датой и возвращает её в правильном формате """
    if len(data) == 20 or 26:
        return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
    return "Некорректный формат даты"
