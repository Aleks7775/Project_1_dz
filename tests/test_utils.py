import unittest
from unittest.mock import mock_open, patch

from src.utils import json_file


class TestReadJsonFile(unittest.TestCase):
    def test_read_json_file_with_data(self):
        """Тесты возвращают ожидаемый список словарей, когда файл содержит корректные данные,
         и пустой список, когда файл пустой или содержит некорректные данные"""
        mock_data = '[{"id": 1, "amount": 100}]'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = json_file('fake_path.json')
            self.assertEqual(result, [{"id": 1, "amount": 100}])

    def test_read_json_file_empty(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = json_file('fake_path.json')
            self.assertEqual(result, [])
