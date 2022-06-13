import time
print("Mostrarei os 10 primeiros termos de uma progressão de acordo com os valores que você apresentar.. ")
termo = int(input("digite o primeiro termo: "))
razao = int(input("digite a razão: "))
valores = termo - razao
contador = 0
cont = 0

while contador != 10:
    valores = (valores + razao)
    if valores < 0:
        print(f"({valores})", end=" - ")
    else:
        print(valores, end=" - ")
    contador += 1

resposta = int(input("\nQuer que eu mostre mais quantos termos? "))

while resposta != 0:
    cont = resposta
    for c in range(0, cont):
        valores = (valores + razao)
        if valores < 0:
            print(f"({valores})", end=" - ")
        else:
            print(valores, end=" - ")
    resposta = int(input("quer ver mais quantos? "))

time.sleep(1.5)
print("fim do programa..")
time.sleep(1.5)
