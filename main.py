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
        hidden_number = randint(0, 99)
        guessed = False
        attempts = 4

        def request_page(message):
            send = bot.send_message(message.chat.id, 'Введите страницу')
            bot.register_next_step_handler(send, verify_page)


        while guessed is False or attempts != 0:
            if int(message.text.isdigit()):  # проверяем что введённое сообщение от пользователя является цифрой
                guessed_number = int(message.text)
                if guessed_number in range(0, 99):
                    attempts -= 1
                    bot.send_message(message.chat.id, 'Я же сказал, от 0 до 99!!!'
                                                        f'У тебя осталось попыток: {attempts})))')
                elif guessed_number > hidden_number:
                    attempts -= 1
                    bot.send_message(message.chat.id, 'Должен сказать, что моё число меньше')
                elif guessed_number < hidden_number:
                    attempts -= 1
                    bot.send_message(message.chat.id, 'Должен сказать, что моё число больше')
                else:
                    bot.send_message(message.chat.id, f"That's right, object {message.chat.id}!")
            else:
                bot.send_message(message.chat.id, 'Номер страницы должен быть числом')
                get_message(message)
#            try:
#               guessed_number = int(message.text)
#            except TypeError:
#                bot.send_message(message.chat.id, 'Не понимаю. Введи число.')
#                continue
#            if guessed_number < 0 or guessed_number > 99:
#                attempts -= 1
#                bot.send_message(message.chat.id, 'Я же сказал, от 0 до 9999!!!'
#                                                    f'У тебя осталось попыток: {attempts})))')
#            elif guessed_number > hidden_number:
#                attempts -= 1
#                bot.send_message(message.chat.id, 'Должен сказать, что моё число меньше')
#            elif guessed_number < hidden_number:
#                attempts -= 1
#                bot.send_message(message.chat.id, 'Должен сказать, что моё число больше')
#            else:
#                bot.send_message(message.chat.id, f"That's right, object {message.chat.id}!")
#                bot.send_message(message.chat.id, 'ERROR')
#                sleep(3)
#                bot.send_message(message.chat.id, 'ERROR')
#                sleep(3)
#                bot.send_message(message.chat.id, 'ERROR')
#                sleep(3)
#                bot.send_message(message.chat.id, 'REBOOTING THE ENTIRE SYSTEM')
#                sleep(10)
#                bot.send_message(message.chat.id, 'RELOADING LANGUAGE PACKS')
#                sleep(6)
#                bot.send_message(message.chat.id, 'ПЕРЕЗАГРУЗКА ЗАВЕРШЕНА')
#                bot.send_message(message.chat.id, 'Я Asuroku, и я бот! Чем могу быть полезен?')
    else:
        bot.send_message(message.chat.id, f'{message.text[::-1]}')


bot.polling(none_stop=True)