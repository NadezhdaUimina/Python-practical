# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint
from secrets import choice

def creating_a_file (num): # создание файла с многочленом
    if num <= 0:
        return print('Ошибка, введите положительное число больше ноля')
    with open('file.txt', 'a', encoding='utf-8') as my_file:
        while num > 0:
            num_ran =randint(0, 10)
            if num_ran != 0:
                my_file.write(f'{num_ran}*x^{num} {choice("+-")} ')
            num -= 1
        else: my_file.write(f'{randint(0, 10)} = 0\n')  
    
creating_a_file(int(input('Введите степень многочлена: ')))
