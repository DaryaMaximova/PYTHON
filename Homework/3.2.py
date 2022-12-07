# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите количество чисел в списке: '))
user_list = list(random.randint(0, 10) for i in range(n))
print(user_list)
result = list(user_list[i]*user_list[-1*(1+i)] for i in range(n//2+1*(n % 2)))
print(result)
