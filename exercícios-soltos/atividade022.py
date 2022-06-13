nome = input('digite seu nome: ').strip()
fullcap = nome.upper()
fulllow = nome.lower()
nospc = nome.split()
print('''Nome com todas maiusculas: {}
Nome com todas minusculas: {}
Letras ao todo sem espaços: {}
Quantidade de letras do primeiro nome: {}'''.format(fullcap, fulllow, len(nome)-nome.count(' '), len(nospc[0])))
