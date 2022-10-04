# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Пример:
# in                       in
# 5                        4
# out                      out
# [10, 2, 3, 8, 9]         [4, 2, 4, 9]
# 22                       8

# from random import sample

# def sum_of_odd_positions (count):  # нахождение суммы на нечетных позициях списка
#     if count < 0:
#         return "Ошибка, введите положительное число"
#     new_list = []
#     sum = 0
#     new_list = sample(range(1, count *2), count)
#     print(new_list)
#     for i in range(0, count, 2):
#         sum += new_list[i]
#     return sum

# result = sum_of_odd_positions(int(input('Введите длину спискa: ')))
# print('Сумма элементов списка, стоящих на нечётных позициях равна:', result)



# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# in                    in
# 4                     5
# out                   out
# [2, 5, 8, 10]         [2, 2, 4, 8, 8]
# [20, 40]              [16, 16, 4]

from random import sample

def new_list (num): #  создание списка
    if num < 0:
        return "Ошибка, введите положительное число"
    list = [] 
    list = sample(range(1, num *2), num)
    return list

def composition (list):  # произведение пар чисел списка
    new_list = []
    len_list = len(list)
    for i in range(len_list//2):
        new_list.append(list[i] * list[(i+1)*(-1)])
    if len_list % 2:
        new_list.append (list[len_list//2])
    return new_list

list = new_list(int(input('Введите длину спискa: ')))
print(list)   
result = composition(list)
print('Произведение пар чисел списка:')
print(result)

