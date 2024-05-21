# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Подключаем модули для переменных окружения
from dotenv import load_dotenv
from os import environ as env
load_dotenv()

# Получаем токен
TOKEN = env['TOKEN']

# Указываем токен
bot = telebot.TeleBot(TOKEN)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Today is the perfect day for new beginnings.", "The best day to decide on a bold act!","Be careful, today the stars can affect your financial condition.","The best time to start a new relationship or deal with old ones.","A fruitful day to deal with accumulated cases."]
second = ["But remember that even in this case, you should not forget about","If you go out of town, think about it in advance", "Those who are aiming to do a lot of things today should remember about","If you have a breakdown, pay attention to","Remember that thoughts are material, this means that during the day you need to constantly think about"]
second_add = ["relationships with friends and family.", "work and business issues that can so inappropriately interfere with plans.","yourself and your health, otherwise complete strife is possible by the evening.","everyday issues — especially those that you didn't finish yesterday.", "rest so as not to turn yourself into a hunted horse at the end of the month."]
third = ["Evil tongues may tell you the opposite, but you don't need to listen to them today.", "Know that success favors only the persistent, so devote this day to educating the spirit.","Even if you cannot reduce the influence of retrograde Mercury, then at least bring things to an end.", "There is no need to be afraid of lonely meetings — today is the time when they mean a lot.", "If you meet a stranger on the way, show concern, and then this meeting will promise you pleasant troubles."]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Hi":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Hi, now I'll tell you the horoscope for today.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Aries', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Taurus', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Gemini', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Cancer', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Leo', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Virgo', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Libra', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Scorpio', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Sagittarius ', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Capricorn', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Aquarius', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Pisces', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Choose your zodiac sign', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write «Hi»")
    else:
        bot.send_message(message.from_user.id, "I don't understand you. Write /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)