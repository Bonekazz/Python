print("Mostrarei os 10 primeiros termos de uma progressão de acordo com os valores que você apresentar.. ")
termo = int(input("digite o primeiro termo: "))
razao = int(input("digite a razão: "))
valores = termo - razao
contador = 0

while contador != 10:
    valores = (valores + razao)
    print(valores, end=" - ")
    contador += 1


