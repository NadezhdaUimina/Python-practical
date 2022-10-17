from user_interface import menu
from print_file import print_csv, print_txt
from writing_file import writing_csv, writing_txt
from search import search




m = menu()
 
if m == 'print_csv': 
    print_csv()
elif m == 'print_txt': 
    print_txt()

if m == 'record_csv':
    writing_csv()
elif m == 'record_txt': 
    writing_txt()

if m == 'search':
    search()


# Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
