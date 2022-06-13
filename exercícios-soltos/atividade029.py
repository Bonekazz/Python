vel = float(input('Velocidade do seu carro na hora da multa: '))
if vel > 80:
    print('''voce ultrapassou o limite de 80km/h.
Baseado na velocidade em que vc estava, sua multa é de R${:.2f}'''.format((vel-80)*7))

    
