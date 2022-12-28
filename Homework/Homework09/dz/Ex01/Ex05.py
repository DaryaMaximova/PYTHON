# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input())
number_neg = -number
def fib(a):
    if a == 0:
        return 0
    elif a in [-1, -2]:
        return -1
    elif a < 0:
        return fib(a + 1) + fib(a + 2)
    elif a in [1, 2]:
        return 1
    else:
        return fib(a-1) + fib(a-2)

result = []

"""for i in range(number_neg, number+1):
    if i < 0:
        result.append(((-1) ** (number + i + 1)) * fib(i))
    else:
        result.append(fib(i))
print(result)"""

result = [((-1) ** (number + i + 1)) * fib(i) if i < 0 else fib(i) for i in range(number_neg, number+1)]

print(result)
