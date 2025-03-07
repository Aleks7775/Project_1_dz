from unittest.mock import Mock, patch

import requests

from src.external_api import convert_in_rub


@patch('requests.get')
def test_convert_in_rub(mock_get):
    """Мокируем успешный ответ API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = 75.50
    mock_get.return_value = mock_response

    """Вызываем функцию с тестовым транзакцией"""
    transaction = {
        'operationAmount': {
            'amount': 10,
            'currency': {
                'code': 'USD'
            }
        }
    }

    """Проверяем результат конвертации"""
    converted_amount = convert_in_rub(transaction)
    assert converted_amount == 75.50

    """Проверяем статус-код ответа"""
    response = requests.get('url')
    assert response.status_code == 200

    """Проверяем результат вызова json()"""
    assert response.json() == 75.50
