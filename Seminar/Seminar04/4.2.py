# Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.
# будем искать число 3 в одной из строк списка

spisok = ["случайная строка 1", "случайная строка 2", "случайная строка 3"]
print(any('4' in row for row in spisok))