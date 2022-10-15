# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи

def beginning (fiel): #первоначальное состояние поля
    print('-------------')
    for i in range(3):
        print(f'  {fiel[0 + i * 3]}   {fiel[1 + i * 3]}   {fiel[2 + i * 3]}')
        print('-------------')
    return fiel

def move_position(field, motion):
    if motion % 2 == 1:
        player = chr(10060)   # x
    else: player = chr(11093)  # o
    pos = int(input(f'Выберете позицию  для {player} (от 1 до 9): '))
    if 0 < pos < 10 and field[pos-1] != chr(10060) and field[pos-1] != chr(11093):
        field[pos-1]= player 
        return field
    else:
        print('Неправильный ввод или поле занято, вы уверены что ввели правильный номер?')
        return 0

def check (res): #проверка на выйгрыш
    win_pos = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_pos:
        if res[i[0]] == res[i[1]] == res[i[2]] == chr(10060):
            return 1
        elif res[i[0]] == res[i[1]] == res[i[2]] == chr(11093):
            return 2
    count = 0
    for i in range(9):
        if res[i] == chr(10060) or res[i] == chr(11093):
            count +=  1
    if count == 9:
        return 3

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
beginning(field)
motion = 1
while motion <= 9:
     
    if move_position(field, motion) == 0:
        motion -= 1
    else: 
        beginning(field)

    if check(field) == 1:
        print(f'Урааааа!!! {chr(10060)} выйграли!!!!')
        break
    elif check(field) == 2:
        print(f'Урааааа!!! {chr(11093)} выйграли!!!!')
        break
    elif check(field) == 3:
        print('Игра окончена. Ничья.')
        break
    motion += 1

