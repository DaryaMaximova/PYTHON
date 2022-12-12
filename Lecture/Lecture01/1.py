# print('hello world')

# ПЕРЕМЕННЫЕ
# # int - целые числа
# # float - вещественные числа
# # boolean - логический тип данных
# # str - строки
# # list - списки

# # Присваиваем значение переменной
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 12334
# print(value)

# # Определяем тип данных
# print(type(a))
# print(type(b))
# print(type(value))

# # Объявление строки
# s = 'hello world'
# s = "hello 'world"
# s = 'hello "world'
# s = 'hello \'world'
# s = 'hello \nworld'  # Переход на новую строку
# print(s)

# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))  # Форматированный вывод данных
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')  # Интерполяция

# # Логический тип данных
# f = True
# print(f)
# f = False
# print(f)

# # Объявление списка
# list = [1, 2, 3]
# print(list)
# list = ['1', '2', '3', 'hello']
# print(list)
# list = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
# print(list)

# Ввод и вывод данных
# print() – отвечает за вывод данных
# input() – отвечает за ввод данных

# Сложение строк
# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# # print(a, b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')
# print(a, ' + ', b, ' = ', a+b)

# Сложение чисел
# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)

# #Сложение вещественных чисел
# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# + сложение
# - вычитание
# * умножение
# / деление
# % деление с остатком
# // целочисленное деление
# ** возведение в степень
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = +123  # унарный плюс
# b = -321  # унарный минус
# c = a+b
# print(c)

# a = 1.3
# b = 3
# c = round(a * b, 3) #округление, в конце количество знаков после запятой
# print(c)

# a = 3
# a = a + 5 #a += 5
# print(a)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# >, >=, <, <=, == (сравнение), != (неравенство)
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in
# a = 1 < 4 and 5 > 2
# print(a)

# func = 1
# T = 4
# x = 123
# print(func < T > (x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)
# is_odd = not f[0] % 2 
# print(is_odd)

#Управляющие конструкции: IF, IF-ELSE

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!')
# else:
#  print('Привет, ', username)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)    

#Управляющие конструкции: WHILE

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
#  print(original)
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

#Управляющие конструкции: FOR

# for i in 1, -2, 3, 14, 5:
#    print(i*2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 5):
#     print(i)    
   
# for i in range(1, 10, 2): #третий аргумент приращение(шаг)
#     print(i)    
    
# for i in 'qwe - rty' :
#     print(i)

#НЕМНОГО О СТРОКАХ
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)
 
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

#ФУНКЦИИ   
 
 #def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

def f(x):
 return x**2
def f(x):
 if x == 1:
   return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType