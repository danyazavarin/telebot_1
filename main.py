import webbrowser

import telebot

bot = telebot.TeleBot("6103651064:AAFZsU649ZVl4i-pxEdn2h4fwccBtUrCqio")


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/danyazavarin')


@bot.message_handler(commands=['start'])
def main(message):
    if message.from_user.first_name is not None and message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.from_user.first_name is None and message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.last_name}')
    elif message.from_user.first_name is not None and message.from_user.last_name is None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Help information")


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, что вы написали')


# bot.infinity_polling()
bot.polling(none_stop=True)
