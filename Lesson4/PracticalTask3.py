# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# in                             in                                            in
# 7                              -1                                            10
# out                            out                                           out
# [4, 5, 3, 3, 4, 1, 2]          Negative value of the number of numbers!      [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [5, 1, 2]                      []                                            [6, 2, 3, 0, 9]


from random import randint

def new_list (num): #  создание списка
    if num < 0:
        return "Ошибка, введите положительное число"
    list = [] 
    for i in range(num):
        list.append(randint(0, 10))
    return list

def checking_for_a_match (list):  #Проверка на совпадение
    new_list = []
    count = 0
    for i in range(len(list)): 
        for j in range(len(list)):
            if list[i] == list[j]:
                count +=1
        if count == 1:
            new_list.append(list[i])
        count = 0
    return new_list

list = new_list(int(input('Введите длину спискa: ')))
print(list)
print('Cписок неповторяющихся элементов: ', checking_for_a_match(list))