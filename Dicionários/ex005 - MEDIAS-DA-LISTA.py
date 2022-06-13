cadastros = list()
pessoa = dict()
mulheres = []
idosos = []
pessoaidosa = []
totalcadastros = 0
somaidades = 0

quantidade = int(input("Digite quantas pessoas quer cadastrar: "))

for c in range(0, quantidade):
    print("==============================")
    print(f"     {c+1}º Pessoa:")
    pessoa['nome'] = str(input("Nome: ")).strip().lower().capitalize()
    pessoa['sexo'] = str(input("sexo: ")).strip().lower()
    while True:
        if pessoa['sexo'] != 'masculino' and pessoa['sexo'] != 'feminino':
            pessoa['sexo'] = str(input("Resposta inválida. Digite o sexo: ")).strip().lower()
        else: 
            break
            
    pessoa['idade'] = int(input("idade: "))
    while True:
        if pessoa['idade'] < 1:
            pessoa['idade'] = int(input("Resposta inválida. Digite a idade: "))
        else:
            break

    
    if pessoa['sexo'] == 'feminino':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] > 59:
        pessoaidosa.append(pessoa['nome'])
        pessoaidosa.append(pessoa['idade'])
        idosos.append(pessoaidosa[:])
        pessoaidosa.clear()
    
    somaidades += pessoa['idade']
    cadastros.append(pessoa.copy())
    pessoa.clear()
    totalcadastros += 1

mediaidade = int(somaidades / quantidade)

print("=============================")
print("    CADASTRO FINALIZADO")
print("=============================")
print(cadastros)

print(f"- Total de pessoas cadastradas: {totalcadastros}")
print("=============================")
print(f"- Média de idade: {mediaidade}")
print("=============================")
if len(mulheres) > 0:
    print("- Mulheres Cadastradas:")
    for c in range(0, len(mulheres)):
        print(f"--- {mulheres[c]}")
    print("=============================")
else:
    print("- Mulheres cadastradas: 0")
    print("=============================")

if len(idosos) == 0:
    print(f"- Pessoas acima da média: 0")
else: 
    print("- Pessoas acima da média: ")
    for c in range(0, len(idosos)):
        print(f"--- {idosos[c]}")

print("FIM DO PROGRAMA")
   


