import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def get_started(message):
    pass


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.chat == 'Привет':
        bot.send_message(message.chat.id, f'Хули {message.chat.irst_name} говоришь')
    else:
        bot.send_message(message.chat.id, f'{message.text[::-1]}')



bot.polling(none_stop=True, interval=10 )