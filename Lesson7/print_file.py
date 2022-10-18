from os import path

def print_csv(): # печать в консоль из файла Lesson7/Phone_book.csv
    file = 'Lesson7/Phone_book.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                print(v.strip())

def print_txt(): # печать в консоль из файла Lesson7/Phone_book.txt
    file = 'Lesson7/Phone_book.txt'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_txt = text.readlines()
            for i, v in enumerate(text_txt):
                print(v.strip())

def print_all():  # запись данных из всех файлов в отдельный фаил Phonebook_all.csv
    file = 'Lesson7/Phone_book_all.csv'
    file_csv = 'Lesson7/Phone_book.csv'
    file_txt = 'Lesson7/Phone_book.txt'
    with open(file, 'w', encoding='utf-8') as text:
        if path.exists(file_csv) and path.exists(file_txt):
            with open(file_csv, 'r', encoding='utf-8') as text_csv,\
                open(file_txt, 'r', encoding='utf-8') as text_txt:
                t_csv = text_csv.readlines()
                text.write(f'Данные из телефонного справочника в фаиле Phonebook.csv!\n\n')
                for i, v in enumerate(t_csv):
                    text.write(f'{v.strip()}\n')
                t_txt = text_txt.readlines()
                text.write(f'\nДанные из телефонного справочника в фаиле Phonebook.txt!\n\n')
                for i, v in enumerate(t_txt):
                    text.write(f'{v.strip()}\n')
                print('Все данные успешно занесены в фаил Phone_book_all.csv')
print_all()