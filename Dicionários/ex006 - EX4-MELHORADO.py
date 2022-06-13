quantidade = int(input("Digite quantos jogadores quer cadastrar: "))
while True:
    if quantidade < 0:
        quantidade = int(input("Resposta inválida. Digite quantos jogadores quer cadastrar: "))
    if quantidade == 0:
        break
    if quantidade > 0:
        jogador = {}
        cadastros = []

        for c in range(0, quantidade):
            jogador['jogador'] = str(input(f"Digite o nome do {c+1}º jogador: "))
            jogador['total-de-gols'] = 0
            partidas = int(input("Quantas partidas ele jogou? "))

            for c in range(0, partidas):
                jogador['partida'+str(c+1)] = int(input(f"Gols na {c+1}º partida: "))
                jogador['total-de-gols'] += jogador['partida'+str(c+1)]
                
            cadastros.append(jogador.copy())
            jogador.clear()

        print("===============================")
        print("    JOGADORES CADASTRADOS")
        print("==============================")

        for c in range(0, len(cadastros)):
                print(f"Nº {c} - {cadastros[c]['jogador']}")
                print(f"Total de gols = {cadastros[c]['total-de-gols']}")
                print("-----------------------------")

        escolha = int(input("Escolha o número do jogador que quer visualizar com detalhes: "))

        print("-----------------------------")
        print(cadastros[escolha])
        continuar = str(input("Deseja continuar? ")).lower().strip()

        while True:
            if continuar == 'sim':
                escolha = int(input("Escolha o número do jogador que quer visualizar com detalhes: "))
                print("-----------------------------")
                print(cadastros[escolha])
                continuar = str(input("Deseja continuar? ")).lower().strip()
            if continuar == 'nao':
                break
            else:
                continuar = str(input("Resposta inválida. Deseja continuar? ")).lower().strip()
    break
print("FIM DO PROGRAMA...")

