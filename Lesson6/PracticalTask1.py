# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
# Use comprehension.
# in                                           in
# 9                                            10
# out                                          out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]               [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [16, 3, 7, 10]                               [24, 15, 23, 25]


from random import sample

def more_then(num):
    list = sample(range(100), num)
    print(list)
    return [list[num] for num in range(1, len(list)) if list[num] > list[num - 1]]


print(f'Cписок, значения которых больше предыдущего элемента:', more_then(int(input('Введите длину спискa: '))))
