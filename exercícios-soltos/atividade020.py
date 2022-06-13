import random
print('digite os nomes dos alunos para sortear a ordem de apresentação: ')
a1 = input('a1: ')
a2 = input('a2: ')
a3 = input('a3: ')
a4 = input('a4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('ordem de apresentação: {}'.format(lista))
