# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from functools import reduce

n = int(input())
numbers = []

"""for i in range(n):
    a = float(input())
    f = a - int(a)
    numbers.append(round(f, 2))
    if f == 0.0:
        numbers.remove(0.0)"""

numbers = [float(input()) for i in range(n)]
print(numbers)

numbers = list(map(lambda x: round(float(x) - int(x), 2), numbers))
print(numbers)

numbers = list(filter(lambda x: float(x) != 0.0, numbers))
print(numbers)

result = 0

max_number = reduce(lambda x, y: x if (x > y) else y, numbers)
print(max_number)

min_number = reduce(lambda x, y: x if (x < y) else y, numbers)
print(min_number)

"""for i in range(len(numbers)):
    if(numbers[i] > max_number):
        max_number = numbers[i]
    else:
        i +=1
print(max_number)


for i in range(len(numbers)):
    if(numbers[i] < min_number):
        min_number = numbers[i]
    else:
        i +=1
print(min_number)"""

result = max_number - min_number
print(result)




