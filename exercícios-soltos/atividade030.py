num = int(input('digite um numero e direi se ele é par ou impar: '))
result = num%2
if result == 0:
    print('{} é par.'.format(num))
else:
    print('{} é ímpar.'.format(num))

