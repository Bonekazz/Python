import datetime
import time

anoatual = datetime.date.today().year
print("Registre abaixo o ano de nascimento de 7 pessoas: ")
time.sleep(1)
maiores = 0
menores = 0

for c in range(1, 8):
    nascimento = int(input("{}ª pessoa: ".format(c)))
    idade = anoatual - nascimento
    if idade >= 18:
        maiores = maiores + 1
        print(" - Maior de idade")
    else:
        menores = menores + 1
        print(" - Menor de idade")

print("Quantidade de maiores de idade: {}".format(maiores))
print("Quantidade de menores de idade: {}".format(menores))


