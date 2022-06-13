list = []

while True:
    num = int(input("Digite um valor: "))
    if num not in list:
        list.append(num)

    continuar = str(input("Deseja continuar? "))
    if continuar == 'nao':
        break

print(sorted(list))
