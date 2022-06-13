sala = float(input('Ola funcionario, digite seu salario: '))
if sala > 1250:
    porcen = 10
if sala <= 1250:
    porcen = 15
aum = float(sala*(porcen/100+1))
if sala > 1250:
    print('''Seu salario é maior que R$1250,00, voce recebeu um aumento de {}%.
Agora seu salario é de R${:.2f}'''.format(porcen, aum))
if sala<= 1250:
    print('''Voce recebeu um aumento de {}%.
Seu salario agora equivale a R${:.2f}.'''.format(porcen, aum))
