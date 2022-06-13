n = 0
contador = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        contador = contador + 1
        n = n + c
print('soma de todos os numero impares multiplos de 3 entre 1 e 500: {}'.format(n))
print('quantidade de numeros achados: {}'.format(contador))
   
    
    
