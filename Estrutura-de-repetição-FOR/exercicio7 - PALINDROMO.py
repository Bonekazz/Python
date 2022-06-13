frase = str(input("digite uma frase, sem acentos: ")).strip().upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = ''

#inv = tudojunto[::-1]
#print(inv)
# esse exercicio é resolvido com este simples codigo kk

for c in range(len(tudojunto) - 1, -1, -1):
    inverso = inverso + tudojunto[c]
if tudojunto == inverso:
    print("Esta frase é um palindromo\n {} = {}".format(tudojunto, inverso))
else:
    print("Esta frase nao é um palindromo\n {} - {}".format(tudojunto, inverso))



