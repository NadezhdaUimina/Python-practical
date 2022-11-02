from random import randint
import telebot
import emoji
import functions_game
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Update, ReplyKeyboardRemove
from config import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

GAME = range(1)

# сoздание игрового поля
def field_play(update, field, _): # игровое поле
    update.message.reply_text(f'-----------------\n'
        f'  {field[0]}     {field[1]}     {field[2]}\n'
        '-----------------\n'
        f'  {field[3]}     {field[4]}     {field[5]}\n'
        '-----------------\n'
        f'  {field[6]}     {field[7]}     {field[8]}\n')

# Обрабатываем команду /start если пользователь отменил разговор
def start(update, _): # Старт
    user = update.message.from_user
    update.message.reply_text(emoji.emojize(f'Привет {user.first_name}!\n'
        'Тебя привествует игра\n:cross_mark: крестики-нолики :hollow_red_circle:.\n\n'
        'Правила игры: Игроки по очереди ставят на свободные клетки поля 3×3 знаки '
        '(один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, ' 
        'горизонтали или диагонали, выигрывает. Первый ход определяется жеребьевкой.\n\n'
        'Давай сыграем!'))  
    return 

# основная часть
def game(update, _):
    user = update.message.from_user
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9] # создание списка

    #определение первого хода жеребьевкой
    if functions_game.one_motion == 'bot': # если по жеребьевке первый ходит бот
        symbol_1 = chr(10060)  # присвоение символа x
        symbol_2 = chr(11093)  # присвоение символа o
        update.message.reply_text(emoji.emojize('Первый ход :cross_mark: делает Бот')) 
        motion = functions_game.bot_motion(field) # ход бота
        field[motion] = symbol_1 # изменение списка в соответсвоо с ходом бота
        update.message.reply_text(f'Бот сделал ход {symbol_1}')
        field_play(update, field, _) # вывод измененного поля в чат

    elif functions_game.one_motion == 'player': # если при жеребьевке первый ходит игрок
        update.message.reply_text(emoji.emojize(f'{user.first_name} первый ход :cross_mark: твой')) 
        field_play(update, field, _) # вывод поля в чат
        symbol_1 = chr(11093)  # присвоение символа o
        symbol_2 = chr(10060)  # присвоение символа x
    keyboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # список кнопок
    markup_key = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)  # создание клавиатуры


    # условие продолжения игры
    while functions_game.check_win(field) != 1 or functions_game.check_win(field) != 2 or functions_game.check_win(field) != 3: 
        
        # ход игрока
        update.message.reply_text(f'{user.first_name}, твой ход {symbol_2}', reply_markup=markup_key) # вывод сообщения в чат
        motion = update.message.text # принимаем данные от игрока
        if field[motion-1].isdigit() == False: # если по данным ввода поле занято, просим ввести новые данные, до тех пор пока не будет введены данные свободной позиции
            while field[motion-1].isdigit() == False:
                update.message.reply_text(f'Поле занято повторите ввод!', reply_markup=markup_key)
                motion = update.message.text # принимаем данные от игрока
        field[motion-1] = symbol_2 # как только введены правельные данные записываем символ
        update.message.reply_text(f'{user.first_name} ход {symbol_2} выполнен')
        field_play(update, field, _) # вывод поля в чат
        
        # ход бота
        motion = functions_game.bot_motion(field) # ход бота
        field[motion] = symbol_1 # изменение списка в соответсвоо с ходом бота
        update.message.reply_text(f'Бот сделал ход {symbol_1}') #оповещение в чат
        field_play(update, field, _) # вывод измененного поля в чат

    # условия выйгрышей
    else:  
        if functions_game.check_win(field) == 1:
            update.message.reply_text(f'Урааааа!!! {chr(10060)} выйграли!!!!', reply_markup=ReplyKeyboardRemove())
        elif functions_game.check_win(field) == 2:
            update.message.reply_text(f'Урааааа!!! {chr(11093)} выйграли!!!!', reply_markup=ReplyKeyboardRemove())   
        elif functions_game.check_win(field) == 3:
            update.message.reply_text(f'Игра окончена! Ничья!', reply_markup=ReplyKeyboardRemove())
    
    return GAME
        
# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    user = update.message.from_user
    
    update.message.reply_text(emoji.emojize(f'Довстречи :waving_hand:\nБудет скучно - пиши.'), reply_markup=ReplyKeyboardRemove()) # Отвечаем на отказ поговорить
    
    return ConversationHandler.END
    
if __name__ == '__main__':
    
    updater = Updater(TOKEN) # Создаем Updater и передаем ему токен вашего бота, токен вставляем в папку config.py
    
    dispatcher = updater.dispatcher # получаем диспетчера для регистрации обработчиков

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler(         
        entry_points=[CommandHandler('start', start)], # точка входа в разговор
        
        states={  # этапы разговора, каждый со своим списком обработчиков сообщений
            GAME: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9)$'), game), CommandHandler('game', game)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()