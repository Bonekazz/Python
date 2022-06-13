extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'deznove','vinte')

numero = int(input("Digite um numero de 0 a 20: "))
while numero < 0 or numero > 20:
    numero = int(input("De 0 a 20, cabron. Digite um numero valido: "))

print(f"Voçê digitou {numero} - '{extenso[numero]}'.")