# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите число: "))
i = 2  # первое простое число
list = []
while i <= N:
    if N % i == 0:
        list.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа : {list}")
