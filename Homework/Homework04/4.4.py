# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень: '))
index = list()
for i in range(1, k+2):
    index.append(randint(1, 100))

poly = list()
for i in range(len(index)):
    if k == 1:
        poly.append(f'{index[i]}*x')
    elif k == 0:
        poly.append(f'{index[i]}')
    else:
        poly.append(f'{index[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        poly.append('+')
    elif flag == 0:
        poly.append('-')
    k -= 1
    
poly.pop(-1)
poly.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(poly))
fout.close()
