nome = input("digite um nome: ")
sexo = input("digite o sexo de {}(M/F): ".format(nome)).strip().upper()
while sexo not in 'MF':
    sexo = input("Você digitou um sexo inválido\n digite novamente: ")
if sexo == 'M':
    sexo = "Masculino"
else:
    sexo = "Feminino"
print("registro:\n-nome: {}\n-sexo: {}".format(nome, sexo))
