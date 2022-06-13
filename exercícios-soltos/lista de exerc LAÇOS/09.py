totalmaior = 0
totalmenor = 0
for c in range(1,9):
    numero = int(input('idade{}: '.format(c)))
    if numero >= 18:
        totalmaior = totalmaior + 1
    elif numero < 18:
        totalmenor = totalmenor  + 1
print('quantidade de pessoas maiores de idade: {}'.format(totalmaior))
print('quantidade de pessoas menores de idade: {}'.format(totalmenor))
    



