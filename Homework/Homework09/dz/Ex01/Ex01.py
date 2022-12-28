# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce

n = int(input())
numbers = []
sum_nechet = 0
"""for i in range(n):
    u = input()
    numbers.append(u)"""

numbers = [input() for i in range(n)]
print(numbers)


"""for i in range(len(numbers)):
    if(int(numbers[i]) % 2 == 0):
       i+=1
    else:
        sum_nechet = int(numbers[i]) + sum_nechet
print(sum_nechet)"""
