import telebot
from telebot.types import Message

BOT_TOKEN = '6700811269:AAHTbD-IEfuz3uWUi8qQnlEeeOa4TWOeN78'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg:Message):
    bot.send_message(msg.chat.id, 'Assalomu alaykum hurmatli webhook foydalanuvchilari !')
