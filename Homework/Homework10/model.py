import pandas as pd
import numpy as np
import seaborn as sns
import csv
import json
from pathlib import Path
import requests
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,)
# from controller import *

# data = open('my_data.csv', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()

CHOICE, SURNAME_EMP, POSITION, HIGH, LOW, IDX_NEW_EMP, LAST_NAME, FIRST_NAME, POS, PHONE_NUMBER, SALARY, DEL_EMP, INDEX, NAME, NEW_DATA, EXP_FILE_JSON, EXP_FILE_CSV = range(17)                   

def start(update, _):
    reply_keyboard = [['Найти сотрудника','Сделать выборку сотрудников по должности', 'Сделать выборку сотрудников по зарплате', 'Добавить сотрудника', 'Удалить сотрудника', 'Обновить данные сотрудника', 'Экспортировать данные в формате json', 'Cancel'],['Найти сотрудника','Сделать выборку сотрудников по должности', 'Сделать выборку сотрудников по зарплате', 'Добавить сотрудника', 'Удалить сотрудника', 'Обновить данные сотрудника', 'Экспортировать данные в формате json', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в справочник сотрудников. Выберите необходимое действие', reply_markup=markup_key)
    return CHOICE

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# импорт данных из csv-файла и json:
def read_csv(update, context):
    dtfr = pd.read_csv('database.csv', sep=',')
    context.user_data['dtfrf'] = dtfr
    update.message.reply_text(dtfr)
    

def read_json(update, context):
    dtfr = pd.read_json('database02.json', lines=True)
    dtfr.head()
    context.user_data['dtfrf'] = dtfr
    update.message.reply_text(dtfr)
    

# экспорт данных в csv-файл и json:
def write_csv(update, context):
    df = context.user_data.get('df')
    print(df)
    df.to_csv ('my_data.csv')
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('my_data.csv', 'rb'))
    return start(update, context)

def write_json(update, context):
    df = context.user_data.get('df')
    print(df)
    json_file = df.to_json(orient='records')
    with open('datab03.json', 'w', encoding='utf-8') as fout:
        fout.write(json_file)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('datab03.json', 'rb'))
    return start(update, context)    

# поиск сотрудника

def find_emp(update, context):
   df = pd.read_json('database02.json', lines=True)
   df.head()
   print(df)
   user = update.message.from_user
   logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
   name = update.message.text
   df = df[df['last_name'] == name]
   print(df)
   df.to_csv ('answ.csv')
   context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
   return start(update, context)

# выборка данных по зарплате и должности
def find_employee_by_position(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    dfr = pd.read_json('database02.json', lines=True)
    dfr.head()
    print(dfr)
    position = update.message.text
    dfr = dfr[dfr['position'] == position]
    print(dfr)
    dfr.to_csv ('answ.csv')
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
    return start(update, context)

def get_salary_range(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел нижнюю границу зарплаты: %s: %s", user.first_name, update.message.text)
    lo = update.message.text
    lo = float(lo)
    context.user_data['low_bound'] = lo
    update.message.reply_text(
            'Введите верхнюю границу зарплаты')
    return HIGH



def find_employees_by_salary_range(update, context):
    df = pd.read_json('database02.json', lines=True)
    df.head()
    print(df)
    user = update.message.from_user
    logger.info("Пользователь ввел верхнюю границу зарплаты: %s: %s", user.first_name, update.message.text)
    hi = update.message.text
    hi = float(hi)
    context.user_data['high_bound'] = hi
    lo = context.user_data.get('low_bound')
    hi = context.user_data.get('high_bound')
    df = df[((df['salary'] > lo) & (df['salary'] < hi))]
    print(df)
    df.to_csv ('answ.csv')
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
    return start(update, context)

# добавление данных о новых сотрудниках
def add_employee_idx(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел индекс сотрудника: %s: %s", user.first_name, update.message.text)
    idx = update.message.text
    context.user_data['id'] = idx
    update.message.reply_text(
            'Введите фамилию нового сотрудника')
    return LAST_NAME

def add_employee_last_name(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел фамилию сотрудника: %s: %s", user.first_name, update.message.text)
    last_name = update.message.text
    context.user_data['last_name'] = last_name
    update.message.reply_text(
            'Введите имя нового сотрудника')
    return FIRST_NAME

def add_employee_first_name(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел имя сотрудника: %s: %s", user.first_name, update.message.text)
    first_name = update.message.text
    context.user_data['first_name'] = first_name
    update.message.reply_text(
            'Введите должность нового сотрудника')
    return POS

def add_employee_position(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел должность сотрудника: %s: %s", user.first_name, update.message.text)
    position = update.message.text
    context.user_data['position'] = position
    update.message.reply_text(
            'Введите номер телефона нового сотрудника')
    return PHONE_NUMBER

def add_employee_phone_number(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел номер телефона сотрудника: %s: %s", user.first_name, update.message.text)
    phone_number = update.message.text
    context.user_data['phone_number'] = phone_number
    update.message.reply_text(
            'Введите размер зарплаты нового сотрудника')
    return SALARY    

def add_employee_salary(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел размер зарплаты сотрудника: %s: %s", user.first_name, update.message.text)
    salary = update.message.text
    context.user_data['salary'] = salary
    idx = context.user_data.get('id')
    last_name = context.user_data.get('last_name')
    first_name = context.user_data.get('first_name')
    position = context.user_data.get('position')
    phone_number = context.user_data.get('phone_number')
    salary = context.user_data.get('salary')

    df1 = pd.DataFrame({'id': [idx], 
    'last_name': [last_name],
    'first_name': [first_name],
    'position': [position],
    'phone_number': [phone_number],
    'salary': [salary]})
    print(df1)
    df = pd.read_json('database02.json', lines=True)
    df.head()
    print(df)
    df = df.append(df1, ignore_index = True)
    print(df)
    df.to_csv ('answ.csv')
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
    update.message.reply_text(df)
    context.user_data['df'] = df
    return start(update, context)   

# удаление данных

def delete_data(update, context):
    df = pd.read_json('database02.json', lines=True)
    df.head()
    print(df)
    user = update.message.from_user
    logger.info("Пользователь ввел фамилию сотрудника: %s: %s", user.first_name, update.message.text)
    name = update.message.text
    pos = df[df['last_name'] == name].index
    if pos:
        df.drop(pos, inplace = True)
        print(df)
        df.to_csv ('answ.csv')
        context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
        update.message.reply_text(df)
        context.user_data['df'] = df
        return start(update, context)
    else:
         update.message.reply_text(
            'Такого сотрудника нет в базе')   

 
# обновление данных
def update_data_ind(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел индекс сотрудника: %s: %s", user.first_name, update.message.text)
    ind = update.message.text
    context.user_data['id'] = ind
    update.message.reply_text(
            'Введите название столбца таблицы')
    return NAME 

def update_data_name(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел данные сотрудника: %s: %s", user.first_name, update.message.text)
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_text(
            'Введите новое значение')
    return NEW_DATA

def update_data(update, context):
    df = pd.read_json('database02.json', lines=True)
    df.head()
    print(df)
    user = update.message.from_user
    logger.info("Пользователь ввел новвые данные сотрудника: %s: %s", user.first_name, update.message.text)
    new_data = update.message.text
    context.user_data['new_data'] = new_data
    ind = context.user_data.get('id')
    name = context.user_data.get('name')
    new_data = context.user_data.get('new_data')
    df.at[ind, name] = new_data
    print(df)
    df.to_csv ('answ.csv')
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('answ.csv', 'rb'))
    update.message.reply_text(df)
    context.user_data['df'] = df
    return start(update, context)        

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться.\n'
        ' Буду тебя ждать.',
    )
    return ConversationHandler.END    

