import pandas as pd
import numpy as np
import seaborn as sns
import csv
import json
from pathlib import Path
from view import (get_salary_range, no_employee_error)

# data = open('datab03.json', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()

# импорт данных из csv-файла и json:
def read_csv():
    df = pd.read_csv('database.csv', sep=',')
    return df

def read_json():
    df = pd.read_json('database02.json', lines=True)
    df.head()
    return df

# экспорт данных в csv-файл и json:
def write_csv(df):
    df.to_csv ('my_data.csv')

def write_json(df):
    json_file = df.to_json(orient='records')
    with open('datab03.json', 'w', encoding='utf-8') as fout:
        fout.write(json_file)

# поиск сотрудника

def find_emp(df):
   name = input('Введите название столбца: ')
   r = input('Введите искомое значение: ')
   df = df[df[name] == r]
   return df

# выборка данных по зарплате и должности
def find_employee_by_position(dfr, position):
    dfr = dfr[dfr['position'] == position]
    return dfr

def find_employees_by_salary_range(df):
    lo, hi = get_salary_range()
    df = df[((df['salary'] > lo) & (df['salary'] < hi))]
    return df

# добавление данных о новых сотрудниках

def add_employee(df):
    idx = input("Введите идентификатор сотрудника: ")
    last_name = input("Введите фамилию сотрудника: ")
    first_name = input("Введите имя сотрудника: ")
    position = input("Введите должность сотрудника: ")
    phone_number = input("Введите номер телефона сотрудника: ")
    salary = input("Введите размер зарплаты сотрудника: ")

    df1 = pd.DataFrame({'id': [idx], 
    'last_name': [last_name],
    'first_name': [first_name],
    'position': [position],
    'phone_number': [phone_number],
    'salary': [salary]})

    df = df.append(df1, ignore_index = True)
    return df

# удаление данных

def delete_data(df):
    name = input('Введите фамилию уволенного сотрудника: ')
    pos = df[df['last_name'] == name].index
    df.drop(pos, inplace = True)
    return df
 
# обновление данных

def update_data(df):
    index = int(input('Введите индекс: '))
    name = input('Введите название столбца: ')
    r = input('Введите новое значение: ')
    df.at[index, name] = r
    return df

