import telebot
from config import TOKEN
from telebot.types import Message
from telebot import types


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def process_start_command(message: Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('☉', '☽', '☿', '♀', '♂')
    markup.row('♃', '♄', '♅', '♆', '♇')
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())





bot.polling()

