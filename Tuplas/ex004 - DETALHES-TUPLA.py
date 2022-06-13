n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
n4 = int(input("Digite um valor: "))
tupla = (n1, n2, n3, n4)
pares = []
for c in range(0,4):
    if tupla[c] % 2 == 0:
        pares.append(tupla[c])

print("==============================================")
print(f"Vezes em que o numero 9 apareceu: {tupla.count(9)}")

if 3 in tupla:
    print(f"O valor 3 foi digitado na posição {tupla.index(3)+ 1}")
else:
    print("O valor 3 não foi encontrado.")

print(f"Numeros pares: {pares}")