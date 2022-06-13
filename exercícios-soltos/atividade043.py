peso = int(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = float(peso/(altura*2))
if imc < 18.5:
    print('vc esta abaixo do peso ideal')
elif 18.5 <= imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')
