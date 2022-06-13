import time

primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))
player = 0

while player != 5:
    time.sleep(2)
    print("=== MENU===\nValor 1: {}\nValor 2: {}\n[1] somar\n[2] multiplicar\n[3] maior entre eles\n[4] novos números\n[5] sair do programa".format(primeiro, segundo))
    player = int(input("O que deseja fazer? "))
    if player == 1:
        soma = primeiro + segundo
        print("Soma entre os valores: {}".format(soma))
        time.sleep(1.3)
    if player == 2: 
        multi = primeiro*segundo
        print("Multiplicação entre os valores: {}".format(multi))
        time.sleep(1.3)
    if player == 3:
        maior = 0
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print("o maior entre eles é {}".format(maior))
        time.sleep(1.3)
    if player == 4:
        print("==== NOVOS NUMEROS ====")
        primeiro = int(input("Digite o primeiro valor: "))
        segundo = int(input("Digite o segundo valor: "))
        time.sleep(1.3)
    if player == 5:
        time.sleep(1)
        print("saindo...")
        time.sleep(2)
    if player > 5:
        print("opção invalida")