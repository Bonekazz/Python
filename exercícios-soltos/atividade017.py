from math import trunc, hypot
print('digite o comprimento do cateto oposto e do cateto adjacente: ')
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print('A hipotenusa deste triangulo retangulo equivale a: {:.2f}'.format((hypot(co, ca))))
