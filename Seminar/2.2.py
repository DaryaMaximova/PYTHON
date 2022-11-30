text = 'Привет, как дела?!'
print(len(text))
rub = len(text)*60//100
print(rub)
kop = len(text)*60 - rub*100
print(kop)
print(f'{rub} р. {kop} коп.')
