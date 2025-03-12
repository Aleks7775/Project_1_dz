import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(input_transactions: list[dict]) -> None:
    """Тест проверяющий корректную фильтрацию транзакций по заданной валюте"""
    generator = filter_by_currency(input_transactions, "USD")
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}
    assert next(generator) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                               'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                               'to': 'Счет 75651667383060284188'}


def test_zero_filter_by_currency(input_transactions: list[dict]) -> None:
    """Проверка функции в случае если не выбрана валюта или выбран пустой список"""
    zero_currency = filter_by_currency(input_transactions)
    assert next(zero_currency) == "Не выбрана валюта"
    zero_currency = filter_by_currency(input_transactions, [])
    assert next(zero_currency) == "Не выбрана валюта"


def test_transaction_descriptions(input_transactions: list[dict]) -> None:
    """Тест проверяющий, что функция возвращает корректные описания для каждой транзакции"""
    generator_transaction = transaction_descriptions(input_transactions)
    assert next(generator_transaction) == "Перевод организации"
    assert next(generator_transaction) == "Перевод со счета на счет"
    generator_transaction = transaction_descriptions([])
    assert next(generator_transaction) == "Транзакции отсутствуют"


def test_card_number_generator() -> None:
    """Тест проверяющий, что генератор выдает правильные номера карт в заданном диапазоне"""
    generator_card_ = card_number_generator(99999, 999999)
    assert next(generator_card_) == "0000 0000 0009 9999"
    assert next(generator_card_) == "0000 0000 0010 0000"
    assert next(generator_card_) == "0000 0000 0010 0001"


def test_final_value_card_number_generator() -> None:
    """Тестирует работу генератора на крайних значениях """
    generator_card = card_number_generator(1, 3)
    assert next(generator_card) == "0000 0000 0000 0001"
    assert next(generator_card) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration):
        next(generator_card)


@pytest.mark.parametrize("start, stop, expected_result", [
    (99999, 100000, "0000 0000 0009 9999"),
    (100000, 100001, "0000 0000 0010 0000"),
    (77777, 88888, "0000 0000 0007 7777")
])
def test_card_generator(start, stop, expected_result) -> None:
    """Тест проверяющий, что генератор выдает правильные номера карт с, использование параметризации"""
    generator = card_number_generator(start, stop)
    assert next(generator) == expected_result
