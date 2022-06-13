print('digite tres numeros:')
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
menor = n1
maior = n2
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
if n3>n1 and n3>n2:
    maior = n3
if n1>n2 and n1>n3:
    maior = n1
print('''Menor valor: {}
Maior valor: {}'''.format(menor, maior))
