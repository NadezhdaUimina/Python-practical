from os import path

def removal():
    removal = input('Введите фамилию для поска удаляемого контакта: ')
    file = 'Lesson7/Phone_book.csv'
    if path.exists(file):
        with open (file, 'r', encoding = 'utf-8') as text:
            count = False
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                if removal in v:
                    v = ''
                    print('Данные из телефонного справочника в фаиле Lesson7/Phone_book.csv были удалены')
                    
                    count = True
            if not count: print('Таких данных нет в справочнике фаила Lesson7/Phone_book.csv')

removal()