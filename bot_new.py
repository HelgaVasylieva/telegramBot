import telebot
from telebot import types
from text import *
from datetime import datetime
from Wmonth import *
# from telegram_bot_calendar import


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
        price_func(callback)

    elif callback.data == 'text2':
        write(callback)

    elif callback.data == 'text4':
        timetable_func(callback)

    elif callback.data == 'text5':
        calendar_start(callback)

    elif callback.data in ls:
        finish(callback)

    elif callback.data == 'start':
        back(callback)

    elif callback.data == 'text6':
        personal(callback)

    else:
        calendar_call(callback)




def price_func(callback):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Повернутись на початок", callback_data='start')
    markup.row(btn)
    bot.send_message(callback.message.chat.id, text=price, reply_markup=markup)


def write(callback):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text5, callback_data='text5')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text6, callback_data='text6')
    markup.row(btn2)

    bot.send_message(callback.message.chat.id, text=f"{callback.message.chat.first_name}, яке тренування цікавить?",
                     reply_markup=markup)



def timetable_func(callback):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Повернутись на початок", callback_data='start')
    markup.row(btn)
    bot.send_message(callback.message.chat.id, text=timetable, reply_markup=markup)


def calendar_start(callback):

    calendar, step = WMonthTelegramCalendar(locale='ukr').build()
    bot.send_message(callback.message.chat.id,
                        f"Обери день",
                        reply_markup=calendar)


@bot.callback_query_handler(func=WMonthTelegramCalendar.func())
def calendar_call(callback):

    result, key, step = WMonthTelegramCalendar(locale='ukr').process(callback.data)

    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              callback.message.chat.id,
                              callback.message.message_id,
                              reply_markup=key)

     # result_new = result.strftime("%d. %m. %Y")

    #result_day = result.strftime("%A")

    elif result:
        result_day = result.strftime("%A")
        result_new = result.strftime("%d. %m. %Y")
        if result_day in list_of_day_1:
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(M1, callback_data='M1')
            markup.row(btn1)

            btn2 = types.InlineKeyboardButton(M3, callback_data='M3')
            markup.row(btn2)

            btn3 = types.InlineKeyboardButton(M4, callback_data='M4')
            markup.row(btn3)

            btn4 = types.InlineKeyboardButton(M5, callback_data='M5')
            markup.row(btn4)

            btn5 = types.InlineKeyboardButton(M5, callback_data='M6')
            markup.row(btn5)

            bot.send_message(callback.message.chat.id, text=f"{callback.message.chat.first_name}, обери групу на {result_new}",
                             reply_markup=markup)


        elif result_day in list_of_day_2:
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(T1, callback_data='T1')
            markup.row(btn1)

            btn2 = types.InlineKeyboardButton(T2, callback_data='T2')
            markup.row(btn2)

            btn3 = types.InlineKeyboardButton(T3, callback_data='T3')
            markup.row(btn3)

            btn4 = types.InlineKeyboardButton(T4, callback_data='T4')
            markup.row(btn4)

            btn5 = types.InlineKeyboardButton(T5, callback_data='T5')
            markup.row(btn5)

            bot.send_message(callback.message.chat.id, text=f"{callback.message.chat.first_name}, обери групу?",
                             reply_markup=markup)


def finish(callback):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Локація', url='https://www.google.com/maps/place/Puncher+Fight+Club+Kyiv/@50.4221595,30.5260693,19.15z/data=!4m6!3m5!1s0x40d4c8d034b088bb:0xb66abd433ccbf8ac!8m2!3d50.4222867!4d30.5255767!16s%2Fg%2F11c55y311w?entry=ttu')
    markup.row(btn)
    rezult = callback.message.text
    for i in range(len(ls)):
        if callback.data == ls[i]:
            ls[i] = ls_1[i]
            text_f = ls_1[i]
            if ls_1[i] in [M1]:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per1} чекає тебе {rezult[-13:-6]} o {text_f[0:5]} на групу {tr1} ",
                                 reply_markup=markup, parse_mode='html')
            elif ls_1[i] in [M3, M4]:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per2}  чекає тебе {rezult[-13:-6]} "
                                      f"o {text_f[0:5]} на групу {tr1} ",
                                 reply_markup=markup, parse_mode='html')
            elif ls_1[i] in [M5, T3, S2]:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per3} чекає тебе {rezult[-13:-6]} "
                                      f"o {text_f[0:5]} на групу {tr1} ",
                                 reply_markup=markup, parse_mode='html')
            elif ls_1[i] == M6:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per4} чекає тебе {rezult[-13:-6]} "
                                      f"o {text_f[0:5]} на групу {tr2} ",
                                 reply_markup=markup, parse_mode='html')
            elif ls_1[i] in [T1, T2, S1]:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per5} чекає тебе {rezult[-13:-6]} "
                                      f"o {text_f[0:5]} на групу {tr1} ",
                                 reply_markup=markup, parse_mode='html')
            elif ls_1[i] == T4:
                bot.send_message(callback.message.chat.id,
                                 text=f"{callback.message.chat.first_name}, тренер {per6} чекає тебе {rezult[-13:-6]} "
                                      f"o {text_f[0:5]} на групу {tr2} ",
                                 reply_markup=markup, parse_mode='html')


def back(callback):
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
        callback.message.chat.id,
        f"Привіт {callback.message.chat.first_name} {callback.message.chat.last_name or ''}!"
        f"Чим можу допомогти?",
        reply_markup=markup
    )

def personal(callback):
    bot.send_message(
        callback.message.chat.id,
        text=f"{per1} \n{per2} \n{per3} \n{per4} \n{per5} \n{per6} \n", parse_mode='html')


bot.infinity_polling()