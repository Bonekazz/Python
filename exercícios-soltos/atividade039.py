idade = int(input('idade: '))
tempoate = 18 - idade
tempoatraso = idade - 18
if idade < 18:
    print('faltam {} ano(s) para seu alistamento no exercito'.format(tempoate))
elif idade > 18:
    print('seu alistamento esta atrasado {} ano(s)'.format(tempoatraso))
else:
    print('Voce esta na idade para o alistamento')
