palavras = ('madeira','a e i', 'carvalho', 'a o','caneta', 'a e', 'palavra', 'a', 'bolha','o a', 'bola', 'o a', 'skate','a e', 'baseado', 'a e o', 'fatos','a o', 'real','e a', 'monitor', 'o i')

for c in range(0, len(palavras), 2):
    print(f"{palavras[c]} possui as vogais: {palavras[c+1]}")
