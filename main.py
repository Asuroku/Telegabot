import telebot
from random import randint
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def get_started(message):
    pass


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, f'Привет, {message.chat.first_name[::-1]}, я ')
    elif message.text == 'Давай поиграем':
        bot.send_message(message.chat.id, f'Ок, {message.chat.first_name}, давай сыграем.'
                                          f'В какую игру ты хочешь сыграть?')
    else:
        bot.send_message(message.chat.id, f'{message.text[::-1]}')



bot.polling(none_stop=True, interval=10 )