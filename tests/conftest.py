import pytest

@pytest.fixture
def bank_product():
    return ['num', '12345', '', {}, [], 1]


@pytest.fixture()
def data_get_format():
    return ["0",'12.12.12.', '', {}, [], ]
