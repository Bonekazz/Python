alunos = {'nome': (input("Digite o nome do aluno: ")), 'media': (float(input("Digite a média do aluno: ")))}
if alunos['media'] >= 7:
    print(f"{alunos['nome']} - APROVADO ")
else:
    print(f"{alunos['nome']} - REPROVADO")