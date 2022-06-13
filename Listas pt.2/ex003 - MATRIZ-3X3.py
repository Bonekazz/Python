matriz = ([], [], [], [], [], [], [], [], [])

for c in range(0,9):
    num = int(input("Digite um valor: "))
    matriz[c].append(num)

print(f"{matriz[0]}{matriz[1]}{matriz[2]}")
print(f"{matriz[3]}{matriz[4]}{matriz[5]}")
print(f"{matriz[6]}{matriz[7]}{matriz[8]}")