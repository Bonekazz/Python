list = []
contador = 0

while True:
    num = int(input("Digite um valor: "))
    contador += 1
    list.append(num)
    
    pergunta = str(input("Deseja continuar? ")).strip().lower()
    if pergunta == 'nao':
        break
    else:
        if 'sim' not in pergunta:
            pergunta = str(input("Resposta invalida. Deseja continuar? ")).strip().lower()

print("="*20)
print(f"- Numero de valores digitados: {contador}.")
list.sort(reverse=True)
print(f"- Valores digitados: {list}.")
if 5 in list:
    print(f"- O valor 5 foi digitado e está na posição: {list.index(5) + 1}.")
else:
    print("- O valor 5 nao foi digitado.")