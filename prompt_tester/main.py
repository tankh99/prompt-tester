import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy friend!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  bot.reply_to(message, message.text)

bot.infinity_polling()