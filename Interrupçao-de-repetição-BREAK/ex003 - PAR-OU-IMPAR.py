import random
import time

cont = 0
while True:
    jogador = str(input("Par ou ímpar? ").strip().lower())
    while jogador not in 'parimpar':
        jogador = str(input("Vc digitou errado. Par ou ímpar? ")).strip().lower()
    computador = random.randrange(0,11)

    valor = int(input("digite seu valor(de 0 a 10): "))
    while valor > 10 or valor < 0:
        valor = int(input("é de 0 a 10 cabron, digite dnv: "))

    resultado = (valor + computador) % 2
    conta = valor + computador
    parimpar = ''
    if resultado == 0:
        parimpar = 'par'
    else:
        parimpar = 'impar'

    if jogador == 'par' and resultado == 0:
        print(f"o computador escolheu {computador}")
        print(f"Vc venceu! deu {conta} e é par")
        cont += 1
    elif jogador == 'impar' and resultado > 0:
        print(f"o computador escolheu {computador}")
        print(f"Vc venceu! deu {conta} e é impar")
        cont += 1
    else:
        print(f"o computador escolheu {computador}")
        print(f"deu {parimpar}")
        print("vc perdeu, boa sorte na proxima cabron")
        time.sleep(0.5)
        print(f"suas vitórias: {cont}")
        break

time.sleep(1)
print("fim do programa...")
time.sleep(1.2)