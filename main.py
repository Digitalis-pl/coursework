from utils import get_executed_operation, open_file
from utils import get_operations, get_last_five, get_necessary_values, show_operations, get_currency, form_our_last_list



operations = open_file()
executed_list = get_executed_operation(operations)
sorted_operations_list = get_operations(executed_list)
last_five_list = get_last_five(sorted_operations_list)
necessary_values_list = get_necessary_values(last_five_list)
currency_list = get_currency(necessary_values_list)
our_last_list = form_our_last_list(necessary_values_list, currency_list)
show_operations(our_last_list)