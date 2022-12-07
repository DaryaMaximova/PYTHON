# РАБОТА С ФАЙЛАМИ
# a - открытие для добавления данных 
# r - открытие для чтения данных 
# w - открытие для записи данных
# r+, w+ - открытие и чтение 

# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# exit() - позволяет не выполнять код ниже 

# ФУНКЦИИ

# def new_string(symbol, count):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# РЕКУРСИЯ

# def fib(n):
#  if n in [1, 2]:
#  return 1
#  else:
#  return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# КОРТЕЖИ

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# a = (3, 4)
# a = (3, ) - кортеж из одного элемента
# print (a)
# print (a[0])
# for item in a:
#     pint(item)

# СЛОВАРИ

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# for k in dictionary.keys(): ключи 
#     print(k)
# for k in dictionary.values(): значения 
#     print(K)
        
# МНОЖЕСТВА 

# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \

# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# СПИСКИ
     
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
    
# list1 = [1, 2, 3, 4, 5]
# print(len(list1))
# print(list1.pop()) - удаление последнего элемента
# print(list1)

# print(list1.insert(2, 11)) - вставление элемента
# print(list1)

# print(list1.append(11)) - добавление элемента в конец
# print(list1)
        
     