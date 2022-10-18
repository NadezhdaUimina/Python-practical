from info import info
from creature import creature_csv, creature_txt

from os import path


 
def writing_csv():   # запись данных в фаил, Lesson7/Phone_book.csv
    i = info()
    file = 'Lesson7/Phone_book.csv'
    if path.exists(file):
        with open (file, 'a', encoding = 'utf-8') as file_csv:
            file_csv.write(f'{i[0]}; {i[1]}; {i[2]}; {i[3]}\n')
            print('Данные успешно добавлены в фаил Lesson7/Phone_book.csv')
    else: 
        creature_csv()
        file_csv.write(f'{i[0]}; {i[1]}; {i[2]}; {i[3]}\n')
        print('Данные успешно добавлены в фаил Lesson7/Phone_book.csv')

def writing_txt():  # запись данных в фаил, Lesson7/Phone_book.txt
    i = info()
    file = 'Lesson7/Phone_book.txt'
    if path.exists(file):
        with open (file, 'a', encoding = 'utf-8') as file_txt:
            file_txt.write(f'Фамилия: {i[0]}\nИмя: {i[1]}\nНомер телефона: {i[2]}\nОписание: {i[3]}\n\n')
            print('Данные успешно добавлены в фаил Lesson7/Phone_book.txt')
    else: 
        creature_txt()
        file_txt.write(f'Фамилия: {i[0]}\nИмя: {i[1]}\nНомер телефона: {i[2]}\nОписание: {i[3]}\n\n')
        print('Данные успешно добавлены в фаил Lesson7/Phone_book.txt')
