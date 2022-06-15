def leaiDinheiro(txt=""):
    din = input(f"{txt} R$").strip()
    a = din.replace(',', '.')
    while True:
        if a.isalpha():
            print(f"{din} não é um número.")
            din = input("Digite novamente: R$").strip()
            a = din.replace(',', '.')
        else:
            return din


    


