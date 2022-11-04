from random import randint
from secrets import choice
from main_game import field


def one_motion():  # очередность хода
    mone_motion = randint(0, 2)
    return 'bot' if mone_motion else 'player'


def bot_motion(field):  # ход бота
    motion_bot = choice(range(9))
    return motion_bot


def check_win(res):  # проверка на выйгрыш или ничью
    win_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_pos:
        if res[i[0]] == res[i[1]] == res[i[2]] == chr(10060):
            return 1
        elif res[i[0]] == res[i[1]] == res[i[2]] == chr(11093):
            return 2
    count = 0
    for i in range(9):
        if res[i] == chr(10060) or res[i] == chr(11093):
            count += 1
    if count == 9:
        return 3
