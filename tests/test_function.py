import os

import pytest

from utils import read_file, sort_5_operatons, masked_number, change_date

PATH = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def test_read_file():
    data = read_file(os.path.join(PATH,'test_operations.json'))
    assert isinstance(data, list)

@pytest.fixture
def test_sort_5_operatons():
  data = [
    {
      "id": 441945886,
      "state": "EXECUTED",
      "date": "2019-08-26T10:50:58.294041",
      "operationAmount": {
        "amount": "31957.58",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Maestro 1596837868705199",
      "to": "Счет 64686473678894779589"
    },
    {
      "id": 41428829,
      "state": "EXECUTED",
      "date": "2019-07-03T18:35:29.512364",
      "operationAmount": {
        "amount": "8221.37",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "MasterCard 7158300734726758",
      "to": "Счет 35383033474447895560"
    },
    {
      "id": 939719570,
      "state": "EXECUTED",
      "date": "2018-06-30T02:08:58.425572",
      "operationAmount": {
        "amount": "9824.07",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 75106830613657916952",
      "to": "Счет 11776614605963066702"
    },
    {
      "id": 587085106,
      "state": "EXECUTED",
      "date": "2018-03-23T10:45:06.972075",
      "operationAmount": {
        "amount": "48223.05",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Открытие вклада",
      "to": "Счет 41421565395219882431"
    }
  ]
  assert sort_5_operatons(data) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                     'operationAmount': {'amount': '31957.58',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                     'to': 'Счет 64686473678894779589'},
                                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                                     'operationAmount': {'amount': '8221.37',
                                                         'currency': {'name': 'USD', 'code': 'USD'}},
                                     'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                                     'to': 'Счет 35383033474447895560'},
                                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                     'operationAmount': {'amount': '9824.07',
                                                         'currency': {'name': 'USD', 'code': 'USD'}},
                                     'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                                     'to': 'Счет 11776614605963066702'},
                                    {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
                                     'operationAmount': {'amount': '48223.05',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


@pytest.fixture
def test_musk_number():
    assert masked_number("Maestro 1596837868705199") == "Maestro 1596 83** ****5199"
    assert masked_number("Счет 64686473678894779589") == "Счет **9589"


#def test_musk_number_type():
    #with pytest.raises(AttributeError):
        #masked_number(1)

@pytest.fixture
def test_change_date():
    assert change_date('2019-08-26T10:50:58.294041') == '26.08.2019'