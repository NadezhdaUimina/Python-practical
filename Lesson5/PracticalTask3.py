# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи

from math import radians


def beginning (): #первоначальное состояние поля
    element = []
    for i in range(1, 10):
        element.append(i)
    return element

# def field (element, num, motion): #построение поля position


def print_field (element): #печать поля
    empty_string = str(20 * '-')
    string_1 = str(f'  {element[0]}     {element[1]}     {element[2]}')
    string_2 = str(f'  {element[3]}     {element[4]}     {element[5]}')
    string_3 = str(f'  {element[6]}     {element[7]}     {element[8]}')

    print(empty_string)
    print(string_1)
    print(empty_string)
    print(string_2)
    print(empty_string)
    print(string_3)
    print(empty_string)

element = beginning()
print_field(element)
num_player = int(input('Введите количество игроков (1 или 2): '))
if num_player == 1: one_player(symbol)
elif num_player == 2: two_players()

def two_players ():  #два игрока
    for i in range(9):
        if i % 2:
            first = int(input('Выберете позицию x (от 1 до 9): '))
            if 0 < first < 10:
                if element[first] != 'x' and element[first] != 'o': element[first] = 'x'
                else: 
                    print('Ошибка, данное поле занято')
                    i -= 1
            else: 
                print('Неправильный ввод, вы уверены что ввели правильный номер?')
                i -= 1
        else:
            second = int(input('Выберете позицию 0 (от 1 до 9): '))
            if 0 < second < 10:
                if element[second] != 'x' and element[second] != 'o': element[second] = 'o'
                else: print('Ошибка, данное поле занято')
                i -= 1
            else: 
                print('Неправильный ввод, вы уверены что ввели правильный номер?')
                i -= 1

for i in range(9/2):
    first = int(input('Выберете позицию x (от 1 до 9): '))
    field(num_player, first)
    print(field)
    second = int(input('Выберете позицию 0 (от 1 до 9): '))
    field(num_player, second)
    print(field)


def field (num_player, position):  #два игрока
    if i % 2:
            if 0 < first < 10:
                if element[first] != 'x' and element[first] != 'o':
                    element[first] = 'x'
                else: print('Ошибка, данное поле занято')
                i -= 1
            else: 
                print('Неправильный ввод, вы уверены что ввели правильный номер?')
                i -= 1
        else:
            second = radians(0,10)
            if 0 < second < 10:
                if element[second] != 'x' and element[second] != 'o':
                    element[second] = 'o'
                else: i -= 1
            else: i -= 1         
            
element = field(element, num, motion) 
print_field(element)
           
        


#     elif num_player == 2:
    
#     elif print('Ошибка, введите количество игроков 1 или 2: ')



# fo
# field(1, 0)

# for check () #проверка на выйгрыш

