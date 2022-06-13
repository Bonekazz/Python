nome = input('digite seu nome: ').strip()
txtspr = nome.split()
print('''Primeiro nome: {}
Ultimo nome: {}'''.format(txtspr[0], txtspr[len(txtspr)-1]))
