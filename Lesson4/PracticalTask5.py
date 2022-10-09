# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!


from random import randint
from secrets import choice

def creating_a_file (num): # создание файла с многочленом
    if num <= 0:
        return print('Ошибка, введите положительное число больше ноля')
    with open('Lesson4/file_2.txt', 'a', encoding='utf-8') as my_file:
        while num > 0:
            num_ran =randint(0, 10)
            if num_ran != 0:
                my_file.write(f'{num_ran}*x^{num} {choice("+-")} ')
            num -= 1
        else: my_file.write(f'{randint(0, 10)} = 0\n')  
    
def file_sum (file_1: str, file_2: str):
    with open(file_1, 'r', encoding='utf-8') as my_file_1, open(file_2, 'r', encoding='utf-8') as my_file_2:
        text_1 = my_file_1.readlines()
        text_2 = my_file_2.readlines()
        
        if len(text_1) == len(text_2):
            with open("Lesson4/new_file.txt", "a", encoding="utf-8") as my_file_3:
                for i in range(len(text_1)):
                    result = text_1[i].split('=')
                    my_file_3.write(f"{result} + {text_2[i]}")
        else: print('Содержимое файлов не совпадает!')


for i in range(3):
    creating_a_file(int(input('Введите степень многочлена: ')))
file_sum("Lesson4/file.txt", "Lesson4/file_2.txt")
