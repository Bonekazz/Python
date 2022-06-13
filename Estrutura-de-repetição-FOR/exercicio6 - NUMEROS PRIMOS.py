numero = int(input("digite um valor e direi se este é primo ou nao: "))
if numero % 2 == 0:
    print("{} nao é um numero primo, pois o resto, de sua divisao por 2, é igual a".format(numero), numero % 2)
else:
    print("{} é um numero primo, pois a sua divisao por 2 nao é exata(diferente de 0).".format(numero))