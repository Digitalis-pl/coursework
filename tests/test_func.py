from utils import get_operations, get_executed_operation, open_file, get_last_five, date_format
from utils import get_currency, form_our_last_list, show_operations, read_operation_currency
from utils import get_necessary_values
OPERATIONS = [
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
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }]
def test_get_operations():
    sorted_operations = get_operations(OPERATIONS)
    assert sorted_operations[0]["date"] == "2019-08-26T10:50:58.294041"
    assert sorted_operations[1]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_operations[2]["date"] == "2019-04-04T23:20:05.206878"
    assert sorted_operations[3]["date"] == "2019-03-23T01:09:46.296404"
    assert sorted_operations[4]["date"] == "2018-06-30T02:08:58.425572"
    assert sorted_operations[5]["date"] == "2018-03-23T10:45:06.972075"


operations = open_file()
def test_get_executed_operation():
  executed_operation = get_executed_operation(operations)
  assert executed_operation[0]['state'] == "EXECUTED"


test_list = [1, 2, 3, 4, 5, 6]
def test_get_last_five():
  operations_list = get_last_five(test_list)
  assert len(operations_list) == 5


d = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}]
def test_get_necessary_values():
  necessary_values_list = get_necessary_values(d)
  assert len(necessary_values_list[1]) == 5


date = "2019-08-26T10:50:58.294041"

def test_date_format():
  right_date = date_format(date)
  assert right_date == "2019.08.26"


valyes_list = [['2019-12-08T22:46:21.935582', 'Открытие вклада', None, 'Счет 90424923579946435907', {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}],
               ['2019-12-07T06:17:14.634890', 'Перевод организации', 'Visa Classic 2842878893689012', 'Счет 35158586384610753655', {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}]]
def test_get_currency():
  currency_list = get_currency(valyes_list)
  assert len(currency_list) == 2


currency_list = [['USD', '41096.24'], ['USD', '48150.39']]

def test_form_our_last_list():
  our_last_list = form_our_last_list(valyes_list, currency_list)
  assert our_last_list[0] == ['2019-12-08T22:46:21.935582', 'Открытие вклада', None, 'Счет 90424923579946435907', 'USD', '41096.24']


our_dict = {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
}
def test_read_operation_currency():
  currency_first_list = read_operation_currency(our_dict)
  assert len(currency_first_list) == 2





