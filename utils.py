import json
import datetime
def open_file():
    with open("operations.json", "r", encoding="utf-8") as f:
        operations_list = json.loads(f.read())
        return operations_list


def get_executed_operation(operations):
    executed_operations_list = []
    for i in operations:
        if i == {}:
            continue
        if 'EXECUTED' in i['state']:
            executed_operations_list.append(i)
    return executed_operations_list


def get_operations(operations: list):
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)


def get_last_five(list):
    return list[0:5]

def get_necessary_values(d):
    necessary_values_list = []
    for i in d:
        keys = ['date', 'description', 'from', 'to', 'operationAmount']
        values1 = [i.get(key) for key in keys]
        necessary_values_list.append(values1)
    return necessary_values_list


def date_format(new_date):
    date_time_obj = datetime.datetime.strptime(new_date,'%Y-%m-%dT%H:%M:%S.%f')
    only_date = date_time_obj.date()
    return (only_date.strftime('%Y.%m.%d'))


def get_currency(necessary_values_list):
    currency_d_list = []
    currency_list = []
    for c in necessary_values_list:
        currency_d_list.append(c[4])
    for m in currency_d_list:
        currency_list.append(read_operation_currency(m))
    return currency_list


def read_operation_currency(our_dict):
    necessary_currency = []
    necessary_currency.append(our_dict.get('currency', {}).get('name'))
    necessary_currency.append(our_dict['amount'])
    return necessary_currency


def form_our_last_list(necessary_values_list, currency_list):
    our_last_list = []
    for i, f in zip(necessary_values_list, currency_list):
        i.pop(4)
        our_last_list.append(i + f)
    return our_last_list


def show_operations(our_last_list):
        for i in our_last_list:
            if i[2] == None:
                our_date = i[0]
                our_description = i[1]
                our_to = i[3]
                our_code = i[4]
                our_amount = i[5]
                print(f"""{date_format(our_date)} {our_description}
{our_to[0:5]}**{our_to[21:]}
{our_code} {our_amount}\n""")
            else:
                our_date = i[0]
                our_description = i[1]
                our_from = i[2]
                our_to = i[3]
                our_code = i[4]
                our_amount = i[5]
                index = our_from.rfind(" ")
                print(f"""{date_format(our_date)} {our_description}
{our_from[:index]}{our_from[index:index+3]} {our_from[index+3:index+7]}** **** {our_from[-5:]} -> {our_to[0:5]}**{our_to[21:]}
{our_code} {our_amount}\n""")
