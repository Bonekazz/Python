import random
def sorteio(lista):
    """
    - A função irá adicionar 5 números aleatórios dentro do parâmetro 'lista'.
        * parâmetro 'lista': deve ser uma lista, vazia ou preenchida.
    """
    for c in range(0, 5):
        lista.append(random.randint(1, 100))
    print(f"Lista aleatoria: {lista}")
def soma(lista):
    """
    - A função irá somar todos os valores pares contidos dentro do parâmetro 'lista'.
    * parãmetro 'lista': deve ser uma lista, vazia ou preenchida.
    """
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    if soma == 0:
        print("Nenhum valor par foi encontrado na lista...")
    else:
        print(f"Soma dos valores pares da lista aleatoria: {soma}")


numeros = []
sorteio(numeros)
soma(numeros)



    

