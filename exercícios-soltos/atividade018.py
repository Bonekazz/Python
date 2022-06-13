from math import sin, tan, cos, sqrt, radians
print('digite um angulo para saber seu seno, cosseno e sua tangente.')
ang = radians(float(input('Angulo: ')))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(ang), cos(ang), tan(ang)))
