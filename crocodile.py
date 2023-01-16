import telebot
bot = telebot.TeleBot("...")
from telebot import types
import random


@bot.message_handler(commands=['start'])
def initial_part(message):
    mark_up = types.ReplyKeyboardMarkup(resize_keyboard=True)
    botton_1 = types.KeyboardButton("Да")
    botton_2 = types.KeyboardButton("Нет")
    botton_3 = types.KeyboardButton("Правила игры")
    mark_up.add(botton_1, botton_2, botton_3)
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}!".format(message.from_user), reply_markup=mark_up)
    bot.send_message(message.chat.id, text="Добро пожаловать в игру Табу! Желаю вам удачной игры!".format(message.from_user), reply_markup=mark_up)
    bot.send_message(message.chat.id, text="Начинаем?".format(message.from_user), reply_markup=mark_up)



@bot.message_handler(content_types=['text'])
def functionality(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    random_word = ["Провалиться", "Отчисление", "Футбол", "Обезьяна", "Брить", "Цветочек", "Мода", "Ангина", "Студент", "Удача", "Наставник", ]
    menu1.add(telebot.types.InlineKeyboardButton(text='👁Посмотреть слово', callback_data='first'))
    menu1.add(telebot.types.InlineKeyboardButton(text='🔄Сменить слово', callback_data='second'))

    if (message.text == "Да"):
        user_first_name = str(message.chat.first_name) #Узнаем имя пользователя и оптравляем его в user_first_name
        msg = bot.send_message(message.chat.id,  text ="" f"😃{user_first_name}, должен правильно объяснить слово.", reply_markup = menu1)

        if "Провалиться" in random_word:
            bot.register_next_step_handler(msg, start_2)

    elif (message.text == "Нет"):
        bot.send_message(message.chat.id, text='Нажмите "Да", когда будете готовы')

    elif (message.text == "Правила игры"):
        c_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Игра начинается, игрок должен объяснить слово.", reply_markup=c_mar)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2 = telebot.types.InlineKeyboardMarkup()
    random_word = ["Провалиться", "Отчисление", "Футбол", "Обезьяна", "Брить", "Цветочек", "Мода", "Ангина", "Студент", "Удача", "Наставник", ]

    if call.data == 'first':
        bot.answer_callback_query(callback_query_id=call.id, text=random.choice(random_word))

    if call.data == 'second':
        bot.answer_callback_query(callback_query_id=call.id, text=random.choice(random_word))


def start_2(message):
    bot.send_message(message.chat.id, 'Верно!'.format(message.text))

bot.polling(none_stop=True) #Бот не останавливается

