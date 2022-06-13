import random
import time


resultados = []
jogadores = {}

time.sleep(1)
print('==========================')
print("   O JOGO VAI COMEÇAR..")
print('==========================')
time.sleep(1)
for c in range(0, 4):
    dado = random.randint(1,6)
    resultados.append(dado)
    jogadores['jogador'+str(c+1)] = dado
    print(f"jogador {c+1} tirou {dado}")
    time.sleep(2)

resultados.sort(reverse=True)

print("="*50)
print("   RANKING DOS JOGADORES")
print("="*50)
time.sleep(0.5)

contador = 0
lidos = []

while contador < 4:
    for p in range(0, 4):
        for k, v in jogadores.items():
            if v == resultados[p] and k not in lidos and p not in lidos:
                time.sleep(0.1)
                print(f"{p+1}º lugar -- {k} com {resultados[p]}")
                contador += 1
                lidos.append(k)
                lidos.append(p)
            else: 
                continue
