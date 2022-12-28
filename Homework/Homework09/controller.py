import requests
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,)
from model import *                   

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, SURNAME_EMP, POSITION, HIGH, LOW, IDX_NEW_EMP, LAST_NAME, FIRST_NAME, POS, PHONE_NUMBER, SALARY, DEL_EMP, INDEX, NAME, NEW_DATA, EXP_FILE_JSON, EXP_FILE_CSV = range(17)                   

def start(update, _):
    reply_keyboard = [['Найти сотрудника','Сделать выборку сотрудников по должности', 'Сделать выборку сотрудников по зарплате', 'Добавить сотрудника', 'Удалить сотрудника', 'Обновить данные сотрудника', 'Экспортировать данные в формате json', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в справочник сотрудников. Выберите необходимое действие', reply_markup=markup_key)
    return CHOICE


def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'Найти сотрудника':
        update.message.reply_text(
            'Введите фамилию сотрудника')

        return SURNAME_EMP

    if user_choice == 'Сделать выборку сотрудников по должности':
        update.message.reply_text(
                'Введите должность')
        return POSITION

    if user_choice == 'Сделать выборку сотрудников по зарплате':
        context.bot.send_message(
            update.effective_chat.id, 'Введите нижнюю границу зарплаты')
        return LOW

    if user_choice == 'Добавить сотрудника':
        update.message.reply_text(
                'Введите индекс нового сотрудника')
        return IDX_NEW_EMP  

    if user_choice == 'Удалить сотрудника':
        update.message.reply_text(
                'Введите фамилию уволенного сотрудника')
        return DEL_EMP   

    if user_choice == 'Обновить данные сотрудника':
        update.message.reply_text(
                'Введите индекс сотрудника с изменившимися данными')
        return INDEX

    if user_choice == 'Экспортировать данные в формате csv':
        return EXP_FILE_CSV 

    if user_choice == 'Cancel':
        return cancel(update, context)            
