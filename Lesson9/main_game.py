from random import randint
import telebot
import emoji
import functions
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Update, ReplyKeyboardRemove
from info import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler



GAME_X, GAME_O = range(2)
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # создание списка



# Обрабатываем команду /start если пользователь отменил разговор
def start(update, _):  # Старт
    user = update.message.from_user
    update.message.reply_text(emoji.emojize(f'Привет {user.first_name}!\n'
                                            'Тебя привествует игра\n:cross_mark: крестики-нолики :hollow_red_circle:.\n\n'
                                            'Правила игры: Игроки по очереди ставят на свободные клетки поля 3×3 знаки '
                                            '(один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, '
                                            'горизонтали или диагонали, выигрывает. \n\n'
                                            'Давай сыграем! Чтобы начать игру введите: /start_game.\n'
                                            'Для выхода наберите "cancel"'))
    
    
    
    return GAME_X



# основная часть
def game_x(update, _):
    global field
    user = update.message.from_user

    update.message.reply_text(functions.field_play(field), reply_markup=functions.keyboard())
    # ход игрока
    functions.keyboard()
    update.message.reply_text(f'{user.first_name}, твой ход {chr(10060)}')  # вывод сообщения в чат
    motion = int(update.message.text)  # принимаем данные от игрока
    # если по данным ввода поле занято, просим ввести новые данные, до тех пор пока не будет введены данные свободной позиции
    while field[motion - 1] == chr(10060) or field[motion - 1] == chr(11093):
        update.message.reply_text(f'Поле занято повторите ввод!')
        motion = int(update.message.text)  # принимаем данные от игрока
    else: 
        field[motion - 1] = chr(10060)  # как только введены правельные данные записываем символ
        update.message.reply_text(functions.field_play(field))  # вывод поля в чат
    # проверка условия выйгрышей
    if functions.check_win == chr(10060):
        update.message.reply_text(f'Урааааа!!! {chr(10060)} выйграли!!!!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    elif functions.check_win == 9:
        update.message.reply_text('Игра окончена! Ничья!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    return GAME_O

def game_o(update, _):
    global field
    # ход бота
    motion_b = functions.bot_motion(field)  # ход бота
    field[motion_b] = chr(11093)  # изменение списка в соответсвоо с ходом бота
    update.message.reply_text(f'Бот сделал ход {chr(11093)} на позицию {motion_b + 1}')  # оповещение в чат
    update.message.reply_text(functions.field_play(field))  # вывод измененного поля в чат
    # проверка условия выйгрышей
    if functions.check_win == chr(11093):
        update.message.reply_text(f'Урааааа!!! {chr(11093)} выйграли!!!!', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    return GAME_X


# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    update.message.reply_text(emoji.emojize(f'Довстречи :waving_hand:\nБудет скучно - пиши.'),
                                  reply_markup=ReplyKeyboardRemove()
        )
    return ConversationHandler.END
        


if __name__ == '__main__':
    updater = Updater(TOKEN)  # Создаем Updater и передаем ему токен вашего бота, токен вставляем в папку config.py

    dispatcher = updater.dispatcher  # получаем диспетчера для регистрации обработчиков

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],  # точка входа в разговор

        states={  # этапы разговора, каждый со своим списком обработчиков сообщений
            GAME_X: [MessageHandler(Filters.text, game_x)],
            GAME_O: [MessageHandler(Filters.text, game_o)]
        },

        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()


