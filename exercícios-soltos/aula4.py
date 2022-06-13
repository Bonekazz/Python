print('digite dois valroes')
n1 = int(input('n1: '))
n2 = int(input('n2: '))
soma = n1 + n2
# Formato complicado = print('A soma entre', n1,'e', n2, 'é igual a {}'.format(soma))
# Formato simples = print('A soma entre {} e {} equeivale a {}'.format(n1, n2, soma))
print('A soma entre {1} e {0} equeivale a {2}'.format(n1, n2, soma))
