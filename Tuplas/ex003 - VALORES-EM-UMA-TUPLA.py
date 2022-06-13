import random
n1 = random.randrange(101)
n2 = random.randrange(101)
n3 = random.randrange(101)
n4 = random.randrange(101)
n5 = random.randrange(101)
tupla = (n1, n2, n3, n4, n5)
maior = n5
menor = n1

for c in range(0,5):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]

print(f"Numeros aleatorios: {tupla}\n=======================\nMaior valor: {maior}\nMenor valor: {menor}")