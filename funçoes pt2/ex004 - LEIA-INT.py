def leiaint(txt="", n=""):
    n = input(txt)
    while True:
        if n.isnumeric():
            n = int(n)
            return n
        else:
            n = input(f"'{n}' não é um numero. Digite novamente: ")
        


numero = leiaint("Digite algo: ")
print(f"voce digitou o numero {numero}")


    
