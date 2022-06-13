def area(largura, comprimento):
    area = largura*comprimento
    print(f"O terreno possui uma área de {area}m²")


largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
area(largura, comprimento)