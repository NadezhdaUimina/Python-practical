from menu import menu  
from print_file import print_csv, print_txt
from print_file import print_all
from writing_file import writing_csv, writing_txt
from search import search
import logg


def tel_guide ():
    m = menu()

 
    if m == 'print_csv': 
        print_csv()
        logg.l_p_csv('Вывод данных из Phone_book.csv в консоль')
    elif m == 'print_txt': 
        print_txt()
        logg.l_p_txt('Вывод данных из Phone_book.txt в консоль')
    elif m == 'print_all':
        print_all()
        logg.l_p_txt('Запись данных из всех файлов в файл Phonebook_all.csv')

    if m == 'record_csv':
        writing_csv()
        logg.l_w_csv('Запись данных в фаил, Lesson7/Phone_book.csv')
    elif m == 'record_txt': 
        writing_txt()
        logg.l_w_txt('Запись данных в фаил, Lesson7/Phone_book.txt')

    if m == 'search':
        search()
        logg.l_s_txt('Поиск контакта')
