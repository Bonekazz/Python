import time
def maior(*nums):
    valores =[]
    for c in nums:
        time.sleep(0.5)
        print(f"{c} ", end='', flush=True)
        valores.append(c)
    print(f"Dos {len(valores)} valores digitados. O maior foi {max(valores)}")
    print("-"*30)
    
    
maior(2, 5, 7, 8)
maior(3 ,9, 4, 5, 6)
maior(9, 5, 22, 10, 11)


#VERSAO COM VALORES DEFINIDOS PELO USÁRIO: 

#def maior(lista):
#    print(f"Valores digitados: {lista}")
#    print(f"De todos os valores, o maior foi {max(lista)}")


#contagem = int(input("Digite quantos numeros deseja analisar: "))
#valores = []
#for c in range(0, contagem):
#    valores.append(int(input(f"Numero{c+1}: ")))
#maior(valores)
