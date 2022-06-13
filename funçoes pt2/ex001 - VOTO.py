def voto(a):
    import datetime
    atual = datetime.date.today().year
    idade = atual - a
    resultado = ''
    if idade < 16:
        return f'{idade} anos = VOTO NEGADO'
    if idade > 60:
        return f'{idade} anos = aposentado - VOTO OPCIONAL'
    if idade == 16 or idade < 18:
        return f"{idade} anos = menor de idade - VOTO OPCIONAL"
    else:
        return f"{idade} anos = VOTO OBRIGATÓRIO"
    


nascimento = int(input("Digite seu ano de nascimento: "))
print(voto(nascimento))
