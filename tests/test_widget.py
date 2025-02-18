import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("bank_prod, mask_bank_prod", [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Счет 35383033474447895560', 'Счет **5560')
])
def test_mask_account_new_card(bank_prod: str, mask_bank_prod: str) -> None:
    """Тестирование правильности маскирования номера карты и счета"""
    assert mask_account_card(bank_prod) == mask_bank_prod


def test_mask_card_number_for_empty(bank_product: list) -> None:
    """Проверка работы функции mask_account_card на различных входных форматах с использованием фикстуры"""
    for bank_prod in bank_product:
        assert mask_account_card(bank_prod) == "некорректный номер карты или счета"


@pytest.mark.parametrize("data_entry, data_out", [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2010-05-12T02:26:18.671407', '12.05.2010')])
def test_get_date(data_entry: str, data_out: str) -> None:
    """Тестирование правильности преобразования даты"""
    assert get_date(data_entry) == data_out


def test_get_date_format(data_get_format: str) -> None:
    """Тестирование правильности преобразования даты с использованием фикстуры"""
    for data in data_get_format:
        assert get_date(data_get_format) == "Некорректный формат даты"
