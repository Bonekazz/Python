import time 

time.sleep(1.2)
print("ESTE CAIXA ELETRONICO POSSUI CEDULAS DE R$50, R$20, R$10 E R$1.")
time.sleep(1)

cinquenta = 0
vinte = 0
dez = 0
um = 0
sobra = 0

valor = int(input("digite o valor a ser sacado: R$"))
while valor <= 0:
    valor = int(input("Digite um valor válido: "))
while True:
    if valor - 50 < 0:
        break
    else:
        valor -= 50
        cinquenta +=1
while True:
    if valor - 20 < 0:
        break
    else:
        vinte += 1
        valor -= 20
while True:
    if valor - 10 < 0:
        break
    else:
        valor -= 10
        dez += 1
while True:
    if valor - 1 < 0:
        break
    else:
        valor -= 1
        um += 1

print(f"notas de R$50: {cinquenta}")
print(f"notas de R$20: {vinte}")
print(f"notas de R$10: {dez}")
print(f"notas de R$1: {um}")
    
