# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

numbers = list()
n = int(input('Введите число N: '))
sum = 0
for i in range (n):
    numbers.append((1+1/n)**n)
    sum += numbers[i]
    n+=1
print (numbers)    
print(sum)
