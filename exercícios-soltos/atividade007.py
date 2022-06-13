mater = str(input('Ola querido Pai/Mãe! :)\n Digite a matéria que deseja saber a média, e abaixo as notas de cada bimestre: '))
b1 = float(input('B1(_Primeiro Bimestre_): '))
b2 = float(input('B2(_Segundo Bimestre_): '))
b3 = float(input('B3(_Terceiro Bimestre_): '))
b4 = float(input('B4(_Terceiro Bimestre_): '))
soma = b1+b2+b3+b4
med = float(soma/4)
print(' =========================================')
print('A média de {} é: {}'.format(mater, med))
if med == 6.0:
    print('Parabéns, aluna(o) você alcançou a média da escola!')
elif med <6:
    print('eita abaixo da media, bora estudar ne campeao')
elif med >6<10:
    print('Uau que nota boa, está acima da média!')
elif med == 10.0:
    print('Incrível, você alcançou a nota máxima!')
          
    
