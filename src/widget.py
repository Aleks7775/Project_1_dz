from masks import get_mask_account, get_mask_card_number
from typing import Union


def mask_account_card(bank_prod: Union[str]) -> str:
    """Функция маскировки номера и счета в банке"""
    if "Счет" in bank_prod:
        return f"Счет {get_mask_account(bank_prod)}"
    else:
        name_card = []
        num_card = []
        for i in bank_prod:
            if i.isdigit():
                num_card.append(i)
            else:
                name_card.append(i)
        return f"{"".join(name_card)} {get_mask_card_number("".join(num_card))}"


def get_date(data: Union[str]) -> str:
    """Функция которая принимает на вход строку с датой и возвращает её в правильном формате """
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


"""Проверка функций"""
bank_account = mask_account_card("Счет 73654108430135874305")
num_card_user = mask_account_card("Visa Platinum 8990922113665229")
print(bank_account)
print(num_card_user)
data_ = get_date("2024-05-11T02:26:18.671407")
print(data_)
