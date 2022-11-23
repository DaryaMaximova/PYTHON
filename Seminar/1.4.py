#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

round (float_number, number_of_decimals)
n=float(input('Введите число '))
num=n*10
if (num%10==0):
    print('нет дробной части')
else: print(int(n*10%10))


N = int(input())
M = N*(-1)
print(M)

while N != M:
    print(N)
    N -= 1
else:
    print(N)
    print('это все')

