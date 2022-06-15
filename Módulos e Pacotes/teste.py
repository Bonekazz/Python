from utilidadesCeV import moeda, dado


num = int(input("Digite um numero: "))
while True:
    if num < 0:
        num = int(input("Respota inválida, o valor digitado deve ser maior que 0. Digite um numero: "))
    else: 
        break

moeda.resumo(num)


