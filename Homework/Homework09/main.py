import requests
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,)
from model import *
from controller import *

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            SURNAME_EMP: [MessageHandler(Filters.text, find_emp)],
            POSITION: [MessageHandler(Filters.text, find_employee_by_position)],
            LOW: [MessageHandler(Filters.text, get_salary_range)],
            HIGH: [MessageHandler(Filters.text, find_employees_by_salary_range)],
            IDX_NEW_EMP: [MessageHandler(Filters.text, add_employee_idx)],
            LAST_NAME: [MessageHandler(Filters.text, add_employee_last_name)],
            FIRST_NAME: [MessageHandler(Filters.text, add_employee_first_name)],
            POS: [MessageHandler(Filters.text, add_employee_position)],
            PHONE_NUMBER: [MessageHandler(Filters.text, add_employee_phone_number)],
            SALARY: [MessageHandler(Filters.text, add_employee_salary)],
            DEL_EMP: [MessageHandler(Filters.text, delete_data)],
            INDEX: [MessageHandler(Filters.text, update_data_ind)],
            NAME: [MessageHandler(Filters.text, update_data_name)],
            NEW_DATA: [MessageHandler(Filters.text, update_data)],
            EXP_FILE_JSON: [MessageHandler(Filters.text, write_json)],
            EXP_FILE_CSV: [MessageHandler(Filters.text, write_csv)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

