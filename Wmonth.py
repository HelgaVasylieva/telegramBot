from telegram_bot_calendar.detailed import *
import datetime




class WMonthTelegramCalendar(DetailedTelegramCalendar):
    first_step = DAY
    days_of_week = {'ukr': ["П", "В", "С", "Ч", "П", "С", "Н"], }
    months = {
        'ukr': ["Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Сер", "Вер", "Жов", "Лис", "Гру"],
    }



