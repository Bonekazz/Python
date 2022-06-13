matriz = ([], [], [], [], [], [], [], [], [])
somapares = 0
somaterceiracoluna = 0
maiorsegundalinha = 0
for c in range(0,9):
    num = int(input("Digite um valor(0-10): "))
    while num > 10 or num < 0:
        num = int(input("Resposta inválida. Digite um valor válido(0-10): "))

    matriz[c].append(num)
    
    if num % 2 == 0:
        somapares += num
    if c == 2 or c == 5 or c == 8:
        somaterceiracoluna += num
    if c == 3:
        maiorsegundalinha = num
    if c == 4 or c == 5:
        if num > maiorsegundalinha:
            maiorsegundalinha = num

print("="*50)
print(f" {matriz[0]}{matriz[1]}{matriz[2] }")
print(f" {matriz[3]}{matriz[4]}{matriz[5]} ")
print(f" {matriz[6]}{matriz[7]}{matriz[8]} ")
print("="*50)
print(f"Soma de todos os valores pares digitados: {somapares}")
print(f"Soma dos valores da terceira coluna: {somaterceiracoluna}")
print(f"O maior valor da segunda linha: {maiorsegundalinha}")
print("="*50)