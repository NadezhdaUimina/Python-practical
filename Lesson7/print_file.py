def print_csv(): # печать в консоль из файла Lesson7/Phone_book.csv
    file = 'Lesson7/Phone_book.csv'
    with open(file, 'r', encoding='utf-8') as text:
        text_csv = text.readlines()
        for i, v in enumerate(text_csv):
           print(v.strip())

def print_txt(): # печать в консоль из файла Lesson7/Phone_book.txt
    file = 'Lesson7/Phone_book.txt'
    with open(file, 'r', encoding='utf-8') as text:
        text_txt = text.readlines()
        for i, v in enumerate(text_txt):
           print(v.strip())


