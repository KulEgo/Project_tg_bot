import telebot
from telebot import types
import webbrowser
from telebot.types import InlineKeyboardMarkup
import random
import requests
import json

bot = telebot.TeleBot('TOKEN')
API = 'API'

@bot.message_handler(commands = ['weather'])
def weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=pattaya&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message,f'сейчас погода в городе Паттайя: {data["main"]["temp"]}')

@bot.message_handler(content_types = ['text','photo'])

def answer(message):
    if message.text != '':
        markup = types.InlineKeyboardMarkup()
        des1 = types.InlineKeyboardButton('Задачки для тренировки))',callback_data= 'Линал')
        des2 = types.InlineKeyboardButton('HELP', callback_data= 'question')
        des4 = types.InlineKeyboardButton('Если прям совсем не понятно, то вот вам анекдот ахахахха))', callback_data='anecdot')
        markup.row(des1,des2)
        markup.row(des4)
        bot.reply_to(message, f'Привет, меня зовут Максим и я способен сделать почти (+-) все, что нужно студенту КНАД), а так же выдавать погоду в Паттайе при помощи команды /weather ахаха',reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def f(callback):
    string = ''
    count = 1
    nado = random.randint(1, 5)
    for i in open('float.txt', encoding='utf-8').readlines():
        if i == '\n':
            count = count + 1
        elif count == nado:
            string += i



    if callback.data == 'Линал':
        markup1 = types.InlineKeyboardMarkup()
        des1 = types.InlineKeyboardButton('Линал, матрицы)', callback_data = 'Линал 1')
        des2 = types.InlineKeyboardButton('Линал, перестановки и что-то там еще,', callback_data = 'Линал 2')
        des3 = types.InlineKeyboardButton('Линал, Определитель', callback_data = 'Линал 3')
        des4 = types.InlineKeyboardButton('Линал, метод Гаусса))',callback_data = 'Линал 4')
        markup1.row(des1, des2)
        markup1.row(des3, des4)
        bot.reply_to(callback.message, f'Эх, не тот путь ты выбрал), еще есть шанс вернуться назад', reply_markup = markup1)

    if callback.data == 'Линал 1':
        bot.send_photo(callback.message.chat.id, 'https://imgur.com/a/cSXx5dE', caption='Лови задания), желаю удачи!', parse_mode='HTML')
    if callback.data == 'Линал 2':
        bot.send_photo(callback.message.chat.id, 'https://imgur.com/a/aeH48VO', caption='Лови задания), желаю удачи!', parse_mode='HTML')
    if callback.data == 'Линал 3':
        bot.send_photo(callback.message.chat.id, 'https://imgur.com/a/2SzjXE0', caption='Лови задания), желаю удачи!', parse_mode='HTML')
    if callback.data == 'Линал 4':
        bot.send_photo(callback.message.chat.id, 'https://imgur.com/a/34Tfiw0', caption='Лови задания), желаю удачи!', parse_mode='HTML')


    if callback.data == 'question':
        bot.send_message(callback.message.chat.id,"Это точно поможет разобраться в материале), https://elar.urfu.ru/bitstream/10995/78551/1/978-5-7996-2776-8_2019.pdf?ysclid=m2ki3o7kpx287508328")

    if callback.data == 'anecdot':
        bot.send_message(callback.message.chat.id, string)
bot.polling(none_stop = True)





