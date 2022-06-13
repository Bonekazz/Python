print('digite 6 numeros: ')
n = 0
lista = 0
for c in range(1, 7):
    numeros = int(input())
    if numeros % 2 == 0:
        lista = lista + numeros

if numeros % 2 == 0:
    n = n + 1
    print('numeros pares:', n)
    print('soma destes numeros pares:', lista)
else:
    print('nao há nenhum numero par')

    
         
