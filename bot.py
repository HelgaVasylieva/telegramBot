import telebot
from telebot import types
from text import *


API_TOKEN = '6161931423:AAGZdo4PASDKbMte4Ehqgfg-vWnhCGppU90'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text1)
    btn2 = types.KeyboardButton(text2)
    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        f"Привіт {message.chat.first_name} {message.chat.last_name or ''}!"
        f"Чим можу допомогти?",
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == text1:
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
        btn1 = types.KeyboardButton(text5)
        btn2 = types.KeyboardButton(text6)
        back = types.KeyboardButton(back_text)
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Які тренування тебе цікавлять?", reply_markup=markup)
    elif message.text == text3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text2)
        back = types.KeyboardButton(back_text)
        markup.add(btn, back)
        bot.send_message(message.chat.id, text=price, reply_markup=markup)
    elif (message.text == back_text):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text1)
        button2 = types.KeyboardButton(text2)
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text=back_text1, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text=dont)






bot.infinity_polling()
