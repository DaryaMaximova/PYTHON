from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from model import *
from spy import *
import datetime

""" token='5805211308:AAEHWGI3Fb0FDxiUvRC0RDuzbpv6Lm7Vp_M'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling() """

app = ApplicationBuilder().token('5805211308:AAEHWGI3Fb0FDxiUvRC0RDuzbpv6Lm7Vp_M').build()

app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
# app.add_handler(CommandHandler('time', time_command))
print('server start')

app.run_polling()