pares = 0
for c in range(1,7):
    numero = int(input("digite um valor: "))
    if numero % 2 == 0:
        pares = pares + numero
print("A soma dos valores (apenas pares) que voce digitou é: {}".format(pares))
