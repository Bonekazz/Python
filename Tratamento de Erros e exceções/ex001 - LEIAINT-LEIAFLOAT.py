def leiaint(txt=''):
    while True:
        try:
            a = int(input(f"{txt}"))
        except ValueError:
            print("Você digitou valores inválidos")
            continue
        else:
            return a

        
def leiafloat(txt=''):
    while True:
        try:
            a = float(input(f"{txt}"))
        except ValueError:
            print("Você digitou valores inválidos")
            continue
        else:
            return a
    

a = leiaint("Digite um valor inteiro: ")          
b = leiafloat("Digite um valor real: ")
print(f"Você digitou o valor inteiro {a} e o valor real {b}")
