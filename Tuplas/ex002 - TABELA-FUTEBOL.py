import time 

time.sleep(1)
teams = ('America-MG', 'Athletico-PR', 'Atletico-GO', 'Atletico-MG', 'Avai', 'Botafogo', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiaba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Chapecoense', 'Santos', 'Sao Paulo')

time.sleep(1)
print("=========== TABELA DO FUT ===========")
for c in range(0, 20):
    print(f"{c+1} - {teams[c]}")
print("====================================")

time.sleep(1)
print(f"5 primeiros colocados: {teams[0:5]}\n----------------------")
print(f"Os ultimos 4 colocados: {sorted(teams[16:20])}\n----------------------")
print(f"{teams.index('Chapecoense') + 1} - Chapecoense\n----------------------")