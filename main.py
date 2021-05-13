import telebot
from random import randint
from time import sleep
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def get_started(message):
    bot.send_message(message.chat.id, 'Я Asuroku, и я бот! Чем могу быть полезен?')


@bot.message_handler(content_types=['text', 'int'])
def get_message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, f'Здравствуй, Объект {message.chat.id}')
    elif message.text == 'Давай поиграем':
        bot.send_message(message.chat.id, f'Ок, {message.chat.first_name[5:3:-1]}{message.chat.first_name[3:]}, '
                                          f'давай сыграем.')
        bot.send_message(message.chat.id, 'Я загадал число в промежутке от 0 до 99. Сможешь угадать?')
        a = randint(0, 99)
        b = False
        pop = 4
        while b == False or pop != 0:
            if message.text < 0 or message.int > 99:
                pop -= 1
                bot.send_message(message.chat.id, 'Я же сказал, от 0 до 9999!!!'
                                                  f'У тебя осталось попыток: {pop})))')
            elif message.text > a:
                pop -= 1
                bot.send_message(message.chat.id, 'Должен сказать, что моё число меньше')
            elif message.text < a:
                pop -= 1
                bot.send_message(message.chat.id, 'Должен сказать, что моё число больше')
            else:
                bot.send_message(message.chat.id, f"That's right, object {message.chat.id}!")
                bot.send_message(message.chat.id, 'ERROR')
                sleep(3)
                bot.send_message(message.chat.id, 'ERROR')
                sleep(3)
                bot.send_message(message.chat.id, 'ERROR')
                sleep(3)
                bot.send_message(message.chat.id, 'REBOOTING THE ENTIRE SYSTEM')
                sleep(10)
                bot.send_message(message.chat.id, 'RELOADING LANGUAGE PACKS')
                sleep(6)
                bot.send_message(message.chat.id, 'ПЕРЕЗАГРУЗКА ЗАВЕРШЕНА')
                bot.send_message(message.chat.id, 'Я Asuroku, и я бот! Чем могу быть полезен?')
    else:
        bot.send_message(message.chat.id, f'{message.text[::-1]}')


bot.polling(none_stop=True)
