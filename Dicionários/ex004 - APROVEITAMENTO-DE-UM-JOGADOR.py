jogador = dict()

jogador['nome'] = str(input("Digite o nome do jogador(a): ")).strip().lower().capitalize()
jogador['total-de-partidas'] = int(input("Quantas partidas foram jogadas? "))

while True:
    if jogador['total-de-partidas'] < 0:
        jogador['total-de-partidas'] = int(input("Resposta inválida. Quantas partidas foram jogadas? "))
    else:
        break

totalgols = 0

for c in range(0, jogador['total-de-partidas']):
    jogador['partida'+str(c+1)] = int(input(f"Gol(s) na {c+1}º partida: "))
    while True:
        if jogador['partida'+str(c+1)] < 0:
            jogador['partida'+str(c+1)] = int(input(f"Resposta inválida. Gol(s) na {c+1}º partida: "))
        else: 
            break
        
    totalgols += jogador['partida'+str(c+1)]

jogador['total-de-gols'] = totalgols

print(f"- Nome: {jogador['nome']}")
print(f"- Total de partidas: {jogador['total-de-partidas']}")
print(f"- Total de gols: {jogador['total-de-gols']}")
    