print('Digite seu salário e a porcentagem de aumento que receberá')
sal = float(input('Salário(R$): '))
pa = float(input('Aumento(%): '))
vf = float(sal*(pa/100+1))
print('Seu Salário com aumento - R${:.2f}'.format(vf))
