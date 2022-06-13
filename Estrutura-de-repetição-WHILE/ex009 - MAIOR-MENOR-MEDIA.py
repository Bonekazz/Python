import time
cont= 0
resposta = 1
maior = 0
menor = 0
soma = 0

while resposta == 1:
    numero = int(input("digite um valor: "))
    cont += 1
    soma += numero
    if numero > maior:
        maior = numero
    if menor == 0:
        menor = numero
    elif numero < menor:
        menor = numero
    resposta = int(input("quer continuar (0 para nao, 1 para sim)? "))
media = soma / cont
time.sleep(1)
print("=======================================")
print("numeros digitados: {}".format(cont))
print("Maior valor: {}\nMenor valor: {}".format(maior, menor))
print(f"Média dos valores: {media}")

