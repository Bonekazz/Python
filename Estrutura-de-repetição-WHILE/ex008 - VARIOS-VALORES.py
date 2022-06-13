cont = 0
soma = 0

numero = int(input("Digite um valor(limite 999): "))
cont += 1
soma += numero

while numero < 999:
    numero = int(input("Digite outro valor(limite 999): "))
    cont += 1
    soma += numero

print("Voce digitou {} numeros, e a soma entre todos eles é {}".format(cont, soma))