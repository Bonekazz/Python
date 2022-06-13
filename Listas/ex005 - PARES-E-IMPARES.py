lista = []
pares = []
impares = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    resposta = str(input("Deseja continuar? ")).strip().lower()
    if resposta == 'nao':
        break
    elif resposta == 'sim':
        continue
    else:
        resposta = str(input("Resposta invalida. Deseja continuar? ")).strip().lower()

print("="*40)
print(f"Todos os valores digitados: {lista}")
print(f"valores Pares digitados: {pares}")
print(f"Valores impares digitados: {impares}")