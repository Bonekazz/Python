cadastros = list()
nomepeso = list()
pesadas = list()
leves = list()

while True:
    pessoa = str(input("Cadastre uma pessoa: "))
    peso = float(input("Qual o peso desta pessoa? "))
    nomepeso.append(pessoa)
    nomepeso.append(peso)
    cadastros.append(nomepeso[:])
    
    if peso >= 80:
        pesadas.append(nomepeso[0])
    else:
        leves.append(nomepeso[0])

    nomepeso.clear()
    continuar = str(input("Deseja continuar? ")).lower().strip()
    if continuar == 'nao':
        break
    elif continuar == 'sim':
        continue
    else:
        continuar = str(input("Resposta inválida. Deseja continuar? ")).lower().strip()

print("="*50)
print(f"Total de pessoas cadastradas: {len(cadastros)}")
print(f"Pessoas acima ou na média de peso: {pesadas}")
print(f"Pessoas abaixo da média de peso: {leves}")