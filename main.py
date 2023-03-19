import webbrowser
import telebot
from telebot import types

# подключаю бота к файлу
bot = telebot.TeleBot("6103651064:AAFZsU649ZVl4i-pxEdn2h4fwccBtUrCqio")


# приветствую по команде
@bot.message_handler(commands=['start'])
def start(message):
    # делаю кнопки
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    # приветствую
    if message.from_user.first_name is not None and message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}',
                         reply_markup=markup)
    elif message.from_user.first_name is None and message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.last_name}', reply_markup=markup)
    elif message.from_user.first_name is not None and message.from_user.last_name is None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
    # обработчик событий
    bot.register_next_step_handler(message, on_click)


# создание действий для событий
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')


# присылаю справку по команде
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Help information")


# пересылаю на свой сайт по команде
@bot.message_handler(commands=['site', 'website'])
def site():
    webbrowser.open('https://github.com/danyazavarin')


# отвечаю на фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # делаю кнопки
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/danyazavarin')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    # реагирую на фото
    bot.reply_to(message, 'Какое интересное фото!', reply_markup=markup)


# задаю действия кнопкам delete и edit
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Изменено', callback.message.chat.id, callback.message.message_id)


# отвечаю на видео
@bot.message_handler(content_types=['video'])
def get_video(message):
    bot.reply_to(message, 'Какое интересное видео!')


# отвечаю на текст
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, что вы написали')


bot.polling(none_stop=True)
