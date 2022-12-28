from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import datetime
from spy import *

async def hello(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}')

async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')    

async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n') 

async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    print(msg)
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')         