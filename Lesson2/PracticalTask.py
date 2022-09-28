# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

n = float(input('ведите число: '))
n = n * 10 ** (len(str(n))-2)
sum = 0
while n > 0:
    sum += n % 10
    n = n//10
else: print(f'Сумма цифр в числе равна: {int(sum)}')


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

# n = int(input('введите целое положительное число: '))
# factorial = 1
# if n == 0:
#     print(factorial)
# elif n > 0:
#     for i in range(n):
#         factorial *= i+1
#         print(factorial, end=(' '))


# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

# numbers = []
# sum = 0
# n = int(input('Введите количество элементов списка: '))
# for i in range(1, n+1):
#     num = round((1 + 1/i)**i)
#     numbers.append(num)
#     sum += num
# print(numbers)
# print(f'Сумма элементов списка равна: {sum}')


# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# > [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# > 15

# n = int(input('Введите количество элементов: '))
# pos1 = int(input('Введите позицию первого элемента: '))
# pos2 = int(input('Введите позицию второго элемента: '))
# numbers = []

# if pos1 < 2*n and pos2< 2*n:
#     for i in range(2*n+1):
#         numbers.append(-n + i)

#     print(numbers)
#     print(f'Провезведение элементов на позициях {pos1} и {pos2} равно: {numbers[pos1-1] * numbers[pos2-1]}')
# else: print('Элементов с данными позициями не существует')



# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# > [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# from random import randint

# numbers = []
# n = int(input('Введите длину списка: '))

# for i in range(n):
#     numbers.append(i)
# print(numbers)

# while i < n:
#     numbers[i] = randint(0, n-1)
#     j = 0 
#     for j in range(i):
#         if numbers[i] == numbers[j]:
#             i -= 1
#     i += 1
# print(numbers)