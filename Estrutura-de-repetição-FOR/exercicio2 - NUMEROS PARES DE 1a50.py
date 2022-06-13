import time

time.sleep(0.9)
print("olá, vou mostrar agora a soma de todos os numeros impares multiplos de 3 entre 1 e 500...")
time.sleep(2)

impar = 0
contador = 0

for c in range(1,501, 2):
    if c % 3 == 0:
        impar = impar + c
        contador = contador + 1

print("quantidade de numeros encontrados: {}".format(contador))
print("a soma de todos estes numeros é: {}".format(impar))


