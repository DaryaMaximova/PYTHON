# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 5 -> 101101
# - 3 -> 11
# - 2 -> 10


import math

dec_number = int(input())
n = 10
bin_number = []
i = 0

for i in range(n):
    while dec_number != 0:
        a = dec_number % 2
        math.trunc(a)
        bin_number.append(a)
        dec_number //= 2
        math.trunc(dec_number)

bin_number.reverse()
print(bin_number)



