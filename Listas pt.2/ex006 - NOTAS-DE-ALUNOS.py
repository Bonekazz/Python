alunos = list([])
cadastros = []

while True:
    nome = str(input("Digite o nome da(o) estudante que quer cadastrar: ")).lower().strip().capitalize()
    nota1 = float(input("Cadastre a primeira nota: "))
    nota2 = float(input("Cadastre a segunda nota: "))
    media = (nota1 + nota2)/2
    cadastros.append(nome)
    cadastros.append(nota1)
    cadastros.append(nota2)
    cadastros.append(media)
    alunos.append(cadastros[:])
    cadastros.clear()

    continuar = str(input("deseja continuar com os cadastros? ")).strip().lower()
    if continuar == 'sim':
        continue
    if continuar == 'nao':
        break
    else:
        continuar = str(input("Resposta inválida. Deseja continuar com os cadastros? ")).strip().lower()

for c in range(0, len(alunos)):
    print("="*50)
    print(f"{c + 1} {alunos[c][0]} - média: {alunos[c][3]}")

while True:
    resposta = str(input("Quer procurar um aluno específico? ")).lower().strip()
    if resposta == 'nao':
        break
    if resposta == 'sim':
        busca = int(input("Digite o numero do aluno: "))
        print(f"{alunos[busca -1][0]} - nota1: {alunos[busca-1][1]} - nota2: {alunos[busca-1][2]} -")
    else: 
        resposta = str(input("Resposta inválida. Quer procurar um aluno específico? ")).lower().strip()
    

print("="*50)
print("FIM DO PROGRAMA")

        

