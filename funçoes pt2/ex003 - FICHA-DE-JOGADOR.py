def ficha(nome='none', gols=0):
    print("============================")
    print(f"Jogador: {nome}")
    print(f"Gols marcados: {gols}")
    print("============================")


jog = input("Digite o nome do jogador: ")
while True:
    if jog.isnumeric():
        jog = input("Resposta inválida. Digite o nome do jogador: ")
    else: 
        break
gols = input("Digite o numero de gols que ele marcou: ")
if gols.isnumeric():
    gols = int(gols)
else: 
    gols = 0
if jog == '':
    ficha(gols=gols)
else:
    ficha(jog, gols)