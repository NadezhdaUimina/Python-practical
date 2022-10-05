# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Пример:
# in                in                        in
# 54                9990                      650
# out               outout
# [2, 3, 3, 3]      [2, 3, 3, 3, 5, 37]       [2, 5, 5, 13]


num = int(input('Введите число: '))
list = []
count = 2
while count <= num:
    if num % count == 0:
        list.append(count)
        num //= count
    else:
        count += 1
print('Простые множители числа:', list)

