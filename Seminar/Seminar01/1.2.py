#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

list_number = []
for i in range(5):
    a=int(input())
    list_number.append(a)
print(list_number)
max=list_number[0]
for i in range(len(list_number)):
   if (list_number[i]>max):

a = [1, 4, 8, 7, 5]
print(max(1, 4, 998, 7, 5))
