# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
f = open('file01.txt', 'a', encoding = 'utf_8')
data = 'Удалить из текста слова, содержащие ""абв""'
f.write(data)
f.close()

f = open ('file01.txt', 'r', encoding = 'utf_8')
str = f.read().split()
print(str)
new_str = [n for n in str if 'абв' not in n]
print(new_str)
f.close()