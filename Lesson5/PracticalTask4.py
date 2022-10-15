# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"


from random import randint


def input_dat(name):   #ход игрока
    quantity = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    
    if quantity < 1 or quantity > 28:
        quantity = int(input(f"{name}, введите корректное количество конфет: "))
    return quantity
    
def print_inf(name, quantity, candies):  #информация о ходе
    print(f"Ходил {name}, он взял {quantity}. Осталось на столе {candies} конфет.")


print('Правила игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
 Все конфеты оппонента достаются сделавшему последний ход.')

candies = 2021
num_player = int((input('Выберети 1 - игра с компьютером, 2 - игра два игрока: ')))
one_motion = randint(0,2)  #очередность

if num_player == 1:
    player = (input('Введите ваше имя: '))
    print(f"Первый ходит {player}") if one_motion else print(f"Первый ходит компьютер")
    while candies > 28:
        if one_motion:
            quantity = input_dat(player)
            candies -= quantity
            print_inf(player, quantity, candies)
            one_motion = 0
        else:
            quantity = candies % 29
            candies -= quantity
            print_inf('компьютер', quantity, candies)
            one_motion = 1
    print(f"Выиграл {player}!!!") if one_motion else print(f"Выиграл компьютер!!!")

elif num_player == 2:
    player_1 = (input('Введите имя первого игрока: '))
    player_2 = (input('Введите имя второго игрока: '))
    print(f"Первый ходит {player_1}") if one_motion else print(f"Первый ходит {player_2}")
    while candies > 28:
        if one_motion:
            quantity = input_dat(player_1)
            candies -= quantity
            print_inf(player_1, quantity, candies)
            one_motion = 0
        else:
            quantity = input_dat(player_2)
            candies -= quantity
            print_inf(player_2, quantity, candies)
            one_motion = 1
    print(f"Выиграл {player_1}!!!") if one_motion else print(f"Выиграл {player_2}!!!")












    
    
          





