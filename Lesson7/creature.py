import logg


def creature_csv():  #  создание файла Phone_book.csv
    file = 'Lesson7/Phone_book.csv'
    with open (file, 'w', encoding = 'utf-8') as file_csv:
            file_csv.write(f'Телефонный справочник\n\n'
            'Фамилия; Имя; № телефона; Описание\n')
            logg.l_c_csv('создание файла Phone_book.csv')

def creature_txt():  #  создание файла Phone_book.txt
    file = 'Lesson7/Phone_book.txt'
    with open (file, 'w', encoding = 'utf-8') as file_csv:
            file_csv.write(f'Телефонный справочник\n\n')
            logg.l_c_txt('создание файла Phone_book.txt')
