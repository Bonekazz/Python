import time 
soma = 0
contador = 0

while True:
    valor = int(input("digite um valor[999 para parar]: "))
    if valor == 999:
        break
    else:
        contador = contador + 1
        soma = soma + valor

print(f"Valores digitados: {contador}\nSoma de todos os valores: {soma}")
time.sleep(1.2)
print("fim do programa...")
time.sleep(1.2)