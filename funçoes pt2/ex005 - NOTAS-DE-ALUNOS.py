def notas(*notas, sit=False):
    """
    / A função irá analisar as notas de alguma turma e retornará a 'Quantidade de notas', 'A maior nota', 'A menor nota', 'Média da turma', e a 'Situação da turma'(opcional).
    -- parâmetro 'notas': notas que serão analisadas.
    -- parâmetro 'sit': (opcional)- 'True' para mostrar a situação da turma. Por padrão será 'False' e não mostrará a situação.
    ==========================
    created by bonekazz ;)
    """
    total = 0
    listanotas = []
    soma = 0
    maior = 0
    menor = 0
    cadastro = {}

    for c in notas:
        soma += c
        total += 1
        listanotas.append(c)

    media = soma / len(notas)
    maior = max(listanotas)
    menor = min(listanotas)
    cadastro['Quantidade-de-notas'] = total
    cadastro['Maior-nota'] = maior
    cadastro['Menor-nota'] = menor
    cadastro['Média-da-turma'] = media

    if sit == False:
        return cadastro
    else:
        if media > 8.8:
            cadastro['Situação-da-turma'] = "EXCELENTE"
            return cadastro
        if media > 7:
            cadastro['Situação-da-turma'] = "BOA"
            return cadastro
        if media >= 6 and media <= 7:
            cadastro['Situação-da-turma'] = "RAZOÁVEL"
            return cadastro
        else:
            cadastro['Situação-da-turma'] = "RUIM"
            return cadastro


turma1 = notas(10, 9, 10, 9 , 9, 8, 10, 9, 9, 9, sit=True)
print(turma1)


