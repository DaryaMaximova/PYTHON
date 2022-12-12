# Метод, отвечающий за инициализацию значений переменных х и y
x = 0 
y = 0 
def init(a, b):
    global x
    global y 
    x = a 
    y = b 
# init(11, 22)
# print(x)
# print(y)

def do_it():
    return x+y