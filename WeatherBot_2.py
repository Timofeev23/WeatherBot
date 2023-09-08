from encodings import utf_8
import datetime as dt
import telebot
from telebot import types
import requests

no_city = ['жопа', 'хер', 'лажа', 'а', 'б']

time = dt.datetime.utcnow() + dt.timedelta(hours = +3)

bot = telebot.TeleBot('5051080320:AAHpAZYbnqzk9zPd8YZiNF6Frk-2Y_wuPnI')

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'
    

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Москва')
    item2 = types.KeyboardButton('Санкт-Петербург')
    item3 = types.KeyboardButton('Евпатория')
    item4 = types.KeyboardButton('Казань')
    item5 = types.KeyboardButton('Екатеринбург')
    item6 = types.KeyboardButton('Сочи')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(m.chat.id, 'Напиши название города, чтобы узнать погоду или выбери предложенный вариант ниже', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower == 'жопа' or 'хер':
        bot.send_message(message.chat.id, f'Мне кажется, что {message.text} это не город')
        file = open('/Users/a.timofeev/Desktop/TeleBot/1/log_weatherbot.txt', 'a', encoding='utf_8')
        file.write(f'{time} - {message.from_user} - {message.text}\n \n')
        file.close
    else:    
        bot.send_message(message.chat.id, f'В городе {message.text} сейчас: {what_weather(message.text)}')
        file = open('/Users/a.timofeev/Desktop/TeleBot/1/log_weatherbot.txt', 'a', encoding='utf_8')
        file.write(f'{time} - {message.from_user} - {message.text}\n \n')
        file.close

bot.infinity_polling()