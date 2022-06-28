import time
while True:
    print("======= PROGRAMA DE CADASTROS =======")
    time.sleep(0.2)
    print("1 --- Novo Cadastro")
    time.sleep(0.2)
    print("2 --- Lista de Cadastros")
    time.sleep(0.2)
    print("3 --- Encerrar Programa")
    time.sleep(0.2)
    print("=====================================")
    time.sleep(0.2)
    escolha = int(input("O que deseja fazer? "))
    time.sleep(0.5)
    if escolha == 1:
        print("======= NOVO CADASTRO =======")
        nome = str(input("Nome: ")).strip().lower()
        idade = str(input("Idade: ")).strip().lower()
        f = open("lista-de-cadastros.txt", "a")
        f.writelines(f"{nome}{idade:_>25} anos\n")
        f.close()
        continue
    if escolha == 2:
        print("======= LISTA DE CADASTROS =======")
        f = open("lista-de-cadastros.txt", "r")
        for l in f:
            print(l)
        f.close()
        print("==================================")
        continue
    if escolha == 3:
        break
    else:
        print(f"'{escolha}' não é uma opção válida" )
time.sleep(0.5)
print("=====================================")
print("FIM DO PROGRAMA...")









