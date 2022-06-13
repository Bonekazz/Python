import random, time


while True:
    quantidade = int(input("Digite quantos jogos quer gerar: "))
    while quantidade < 0:
        quantidade = int(input("Quantidade inválida. Digite quantos jogos quer gerar: "))
    if quantidade == 0:
        break

    print("="*50)
    for c in range(0, quantidade):
        time.sleep(2.0)
        print(f"jogo {c + 1} = {list(random.sample(range(61), 6))}")
    print("="*50)

    continuar = str(input("Deseja continuar? ")).lower().strip()
    if continuar == 'nao':
        break
    if continuar == 'sim':
        continue
    else:
        continuar = str(input("Resposta inválida. Deseja continuar? ")).lower().strip()

print("="*50)
print("FIM DO PROGRAMA")
print("="*50)