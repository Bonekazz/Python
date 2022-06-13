maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Digite o peso(kg) da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = 0
            maior = maior + peso
        if peso < maior and peso < menor:
            menor = peso
print("="*20)
print("o maior peso: {}kg\no menor peso: {}kg".format(maior, menor))
