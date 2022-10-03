# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Пример:
# in                       in
# 5                        4
# out                      out
# [10, 2, 3, 8, 9]         [4, 2, 4, 9]
# 22                       8

from random import sample

def sum_of_odd_positions (count):  # нахождение суммы на нечетных позициях списка
    if count < 0:
        return "Ошибка введите положительное число"
    new_list = []
    sum = 0
    new_list = sample(range(1, count *2), count)
    print(new_list)
    for i in range(0, count, 2):
        sum += new_list[i]
    return sum

result = sum_of_odd_positions(int(input('Введите длину спискa: ')))
print('Сумма элементов списка, стоящих на нечётных позициях равна:', result)
