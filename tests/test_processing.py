import pytest
from src.processing.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(op['state'] == 'EXECUTED' for op in result)

    result_canceled = filter_by_state(sample_data, state="CANCELED")
    assert len(result_canceled) == 2
    assert all(op['state'] == 'CANCELED' for op in result_canceled)

def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    assert result[0]['date'] == '2019-07-03T18:35:29.512364'
    assert result[-1]['date'] == '2018-06-30T02:08:58.425572'

    result_ascending = sort_by_date(sample_data, reverse=False)
    assert result_ascending[0]['date'] == '2018-06-30T02:08:58.425572'
    assert result_ascending[-1]['date'] == '2019-07-03T18:35:29.512364'
