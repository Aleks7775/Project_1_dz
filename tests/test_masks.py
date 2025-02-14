from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize("num_cards, expected_mask", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('1234567891234567', '1234 56** **** 4567')])

def test_mask_card_number(num_cards, expected_mask):
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(num_cards) == expected_mask



def test_mask_card_number_for_empty(data_entry):
    """Проверка работы функции get_mask_card_number на различных входных форматах с использованием фикстуры"""
    for num_card in data_entry:
        assert get_mask_card_number(num_card) == "некорректный номер карты"

@pytest.mark.parametrize("num_account, expected_mask", [
    ('73654108430135874305', '**4305'),
    ('12345678912345678912', '**8912')])

def test_mask_account(num_account, expected_mask):
    """Тестирование правильности маскирования номера счёта"""
    assert get_mask_account(num_account) == expected_mask


def test_mask_account_for_empty(data_entry):
    """Проверка работы функции get_mask_account на различных входных форматах с использованием фикстуры"""
    for num_account in data_entry:
        assert get_mask_account(num_account) == "некорректный номер счёта"
