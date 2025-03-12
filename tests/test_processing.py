from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_state_executed: list[dict]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert  filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]) == filter_state_executed


def test_by_state(state_zero: list[dict]) -> None:
    """Тестирование при отсутствии state"""
    assert filter_by_state([{'id': 41428829, 'no_state': 'EXECUTED',
                             'date': '2019-07-03T18:35:29.512364'}]) == state_zero
    assert filter_by_state([]) == []


def test_sort_by_date(sort_date: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам по возрастанию и убывания, а также пустым списком"""
    assert sort_by_date(sort_date) ==  [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                        {"id": 939719570, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"}]

    assert sort_by_date(sort_date, False) == [
                                       {"id": 939719570, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"},
                                       {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                       {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                       {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]

    assert sort_by_date([]) == []
