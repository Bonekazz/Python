import moeda

num = int(input("Digite um numero: "))
print(f"O dobro de {num} é {moeda.dobro(num)}")
print(f"A metade de {num} é {moeda.metade(num)}")
print(f"{num} sofreu um aumento de 10% e resultou em {moeda.aumento(num, 10)}")
print(f"{num} ganhou um desconto de 30% e resultou em {moeda.desconto(num, 30)}")
print(f"{num} em euros -- {moeda.moeda(num, 'euro')}")
print(f"{num} em reais -- {moeda.moeda(num, 'real')}")
print(f"{num} em dolares -- {moeda.moeda(num, 'dolar')}")