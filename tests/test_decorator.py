import pytest

from src.decorators import log, log_func


def test_log():
    """Тест проверяющий корректную работу декоратора"""
    @log()
    def log_funk(a, b):
        return a + b

    result = log_funk(3, 5)
    assert result == 8


def test_log_func(capsys):
    """Тест проверяющий корректную работу декоратора с использованием фикстуры capsys"""
    log_func(2, 5)
    captured = capsys.readouterr()
    assert "ok" in captured.out


def test_log_error(capsys):
    """Тест проверяющий исключение """
    with pytest.raises(TypeError):
        log_func()
    captured = capsys.readouterr()
    assert "log_func error" in captured.out
