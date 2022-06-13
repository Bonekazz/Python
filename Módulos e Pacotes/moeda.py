def aumento(num, porcent):
    aumento = num * (1 + (porcent/100))
    return aumento



def desconto(num, porcent):
    desconto = num * (1 - (porcent/100))
    return desconto


def dobro(num):
    dobro = num * 2
    return dobro


def metade(num):
    metade = int(num / 2)
    return metade


def moeda(num=0, coin=''):
    numero = float(num)
    result = ''
    if coin == 'euro':
        result = f"£{numero}"
        return result
    if coin == 'real':
        result = f"R${numero}"
        return result
    if coin == 'dolar':
        result = f"${numero}"
        return result
