import pytest

@pytest.fixture
def data_entry():
    return ['num', '12345', '', {}, [], 1]


