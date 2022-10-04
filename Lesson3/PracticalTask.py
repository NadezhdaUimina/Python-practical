# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Пример:
# in                       in
# 5                        4
# out                      out
# [10, 2, 3, 8, 9]         [4, 2, 4, 9]
# 22                       8

# from random import sample

# def new_list (num): #  создание списка
#     if num < 0:
#         return "Ошибка, введите положительное число"
#     list = [] 
#     list = sample(range(1, num *2), num)
#     return list

# def sum (list):  # нахождение суммы на нечетных позициях списка
#     sum = 0
#     for i in range(0, len(list), 2):
#         sum += list[i]
#     return sum

# list = new_list(int(input('Введите длину спискa: ')))
# print(list)   
# print('Сумма элементов списка, стоящих на нечётных позициях равна:', sum(list))



# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# in                    in
# 4                     5
# out                   out
# [2, 5, 8, 10]         [2, 2, 4, 8, 8]
# [20, 40]              [16, 16, 4]

# from random import sample

# def new_list (num): #  создание списка
#     if num < 0:
#         return "Ошибка, введите положительное число"
#     list = [] 
#     list = sample(range(1, num *2), num)
#     return list

# def composition (list):  # произведение пар чисел списка
#     new_list = []
#     len_list = len(list)
#     for i in range(len_list//2):
#         new_list.append(list[i] * list[(i+1)*(-1)])
#     if len_list % 2:
#         new_list.append (list[len_list//2])
#     return new_list

# list = new_list(int(input('Введите длину спискa: ')))
# print(list)   
# result = composition(list)
# print('Произведение пар чисел списка:')
# print(result)



# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# Пример:
# in              in             
# 88              11
# out             out
# 1011000         1011

# def number_conversion (num):   # преобразование десятичного числа в двоичное
#     list = []
#     while num > 0:
#         list.insert(0, num % 2)
#         num //= 2

#     result = 0
#     len_list = len(list)
#     for i in range(len_list):
#         result += list[len_list-1-i] * 10**i

#     return result

# result = number_conversion(int(input('Введите число: ')))
# print(result)



# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# from random import uniform

# def new_list (num): #  создание списка
#     if num < 0:
#         return "Ошибка, введите положительное число"
#     list = [] 
#     for i in range(num):
#         list.append(round(uniform(0, 10), 2))
#     return list

# def difference_max_min (list):
#     min = 10
#     max = 0
#     for i in range(0, len(list)):
#         if list[i] % 1 < min:
#             min = list[i] % 1
#         elif list[i] % 1 > max:
#             max = list[i] % 1
#     print('маx значение дробной части', round(max, 2))
#     print('мin значение дробной части', round(min, 2))
#     print('разница между мах и мin значением дробной части:', round(max - min, 2))

# list = new_list(int(input('Введите длину спискa: ')))
# print(list)  
# difference_max_min(list)




# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# Пример:
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def new_list (num): #  создание списка
    list = [] 
    
    if num > 0:
        fib1, fib2 = 1, 1
        for i in range(0, num):
            list.append(fib1)
            fib1, fib2 = fib2, fib1 + fib2
        fib1, fib2 = 0, 1
        for i in range(0, num+1):
            list.insert(0, fib1)
            fib1, fib2 = fib2, fib1 - fib2
        return list

print(new_list(int(input('Введите длину спискa Негафибоначчи: '))))