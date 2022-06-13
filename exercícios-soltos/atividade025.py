nome = input('Estamos procurando alguem da familia Silva, digite o seu nome: ')
resposta = 'Silva' in nome
if resposta == True:
    print('ahh Voce eh da familia Silva, por favor me acompanhe...')
elif resposta == False:
    print('Voce nao eh da familia Silva, pode ir se quiser...')
