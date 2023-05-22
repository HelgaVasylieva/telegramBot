import telebot
from telebot import types
from text import *


API_TOKEN = '6161931423:AAGZdo4PASDKbMte4Ehqgfg-vWnhCGppU90'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(ask, url='https://t.me/Helga_W')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text2, callback_data='text2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton(text3, callback_data='text3')
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton(text4, callback_data='text4')
    markup.row(btn4)


    bot.send_message(
        message.chat.id,
        f"Привіт {message.chat.first_name} {message.chat.last_name or ''}!"
        f"Чим можу допомогти?",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):

    if callback.data == 'text3':
        bot.send_message(callback.message.chat.id, text=price)

    elif callback.data == 'text2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text5, callback_data='text5')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(text6, callback_data='text6')
        markup.row(btn2)

        bot.send_message(callback.message.chat.id, text=f"{callback.message.chat.first_name}, яке тренування цікавить?", reply_markup=markup)
    elif callback.data == 'text4':
        bot.send_message(callback.message.chat.id, text=timetable)



@bot.callback_query_handler(func=lambda callback:True)
def callback_message1(callback):
    if callback.data == 'text5':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("ПН")
        btn2 = types.InlineKeyboardButton("ВТ")
        btn3 = types.InlineKeyboardButton("СР")
        btn4 = types.InlineKeyboardButton("ЧТ")
        btn5 = types.InlineKeyboardButton("Пт")
        btn6 = types.InlineKeyboardButton("СБ")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(callback.message.chat.id, text="Обери день", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == ask:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text3)
        btn2 = types.KeyboardButton(text4)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Що тебе цікавить?", reply_markup=markup)

    elif message.text == text2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text5)
        btn2 = types.KeyboardButton(text6)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Які тренування тебе цікавлять?", reply_markup=markup)
    elif message.text == text4:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text2)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text=timetable, reply_markup=markup)
    elif message.text == text3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text2)
        back = types.KeyboardButton(back_text)
        markup.add(btn, back)
        bot.send_message(message.chat.id, text=price, reply_markup=markup)

    elif message.text == text5:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ПН")
        btn2 = types.KeyboardButton("ВТ")
        btn3 = types.KeyboardButton("СР")
        btn4 = types.KeyboardButton("ЧТ")
        btn5 = types.KeyboardButton("Пт")
        btn6 = types.KeyboardButton("СБ")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Обери день", reply_markup=markup)

    elif message.text == "ПН" or message.text == "СР" or message.text == "Пт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(M1)
        btn2 = types.KeyboardButton(M2)
        btn3 = types.KeyboardButton(M3)
        btn4 = types.KeyboardButton(M4)
        btn5 = types.KeyboardButton(M5)
        btn6 = types.KeyboardButton(M6)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Обери час", reply_markup=markup)

    elif message.text == "ВТ" or message.text == "ЧТ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(T1)
        btn2 = types.KeyboardButton(T2)
        btn3 = types.KeyboardButton(T3)
        btn4 = types.KeyboardButton(T4)
        btn5 = types.KeyboardButton(T5)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Обери час", reply_markup=markup)

    elif message.text == "СБ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(S1)
        btn2 = types.KeyboardButton(S2)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Обери час", reply_markup=markup)

    elif message.text in ls:

        bot.send_message(
            message.chat.id,
            f"{message.chat.first_name} чекаємо, тебе у Puncher на {message.text}"
            )


    elif (message.text == back_text):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(ask)
        button2 = types.KeyboardButton(text2)
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text=back_text1, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text=dont)






bot.infinity_polling()
