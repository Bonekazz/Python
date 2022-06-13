somaidades = 0
media = 0
maisvelho = ''
idademaisvelho = 0
mulheresnovas = 0
for c in range(1,5):
    nome = str(input("Nome: ")).strip()
    idade = int(input("idade: "))
    sexo = str(input("sexo: "))
    somaidades += idade
    
    if c == 1 and sexo in 'masc':
        maisvelho = nome
        idademaisvelho = idade 
    if idade > idademaisvelho and sexo in 'masc':
        maisvelho = nome
        idademaisvelho = idade
    if idade < 20 and sexo in 'fem':
        mulheresnovas += 1



media = somaidades / 4
print("a médias das idades é de {}".format(media))
print("o mais velho é {}".format(maisvelho))
print("Quantidade de mulheres com menos de 20 anos: {}".format(mulheresnovas))
    
    
