lista = ([], [])

for c in range(0,7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        lista[1].append(num)
    else:
        lista[0].append(num)

print("="*50)
print(f"Numeros impares: {lista[0]}")
print(f"Numeros pares: {lista[1]}")