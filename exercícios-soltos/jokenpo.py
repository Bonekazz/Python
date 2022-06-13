import random
numero = input('pedra, papel ou tesoura? ').lower().strip()    
escolhas = 'pedra' or 'papel' or 'tesoura'
pc = random.randrange(2)
if pc == 0:
    escolhas = 'pedra'
elif pc == 1:
    escolhas = 'papel'
elif pc == 2:
    escolhas = 'tesoura'

print('''o computador escolheu {}
voce esoclheu {}'''.format(escolhas, numero))


if numero == 'pedra' and pc == 0:
    print('empate')
elif numero == 'pedra' and pc == 1:
    print('voce perdeu')
elif numero == 'pedra' and pc == 2:
    print('voce ganhou')
    
if numero == 'papel' and pc ==0:
    print('voce ganhou')
elif numero == 'papel' and pc == 1:
    print('empate')
elif numero == 'papel' and pc == 2:
    print('voce perdeu')
    
if numero == 'tesoura' and pc == 0:
    print('voce perdeu')
elif numero == 'tesoura' and pc == 1:
    print('voce ganhou')
elif numero == 'tesoura' and pc == 2:
    print('empate')


