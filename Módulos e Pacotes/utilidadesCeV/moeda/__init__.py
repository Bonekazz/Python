def aumento(num, porcent, moed=''):
    """
    /Calculo de aumentos em porcentagem
    -- parâm. num: número base;
    -- parâm. porcent: porcentagem de aumento que será aplicada;
    -- parâm. moed: opcional; (deve ser escrita entre ''); opções: 'real', 'dolar', 'euro'; retornará a moeda do resultado;
    """
    aumento = str(float(num * (1 + (porcent/100)))).replace(".",",")
    if moed == '':
        return aumento
    else:
        return moeda(aumento, moed)


def desconto(num, porcent, moed=''):
    """
    /Calculo de descontos em porcentagem
    -- parâm. num: número base;
    -- parâm. porcent: porcentagem de desconto que será aplicada;
    -- parâm. moed: opcional; (deve ser escrita entre ''); opções: 'real', 'dolar', 'euro'; retornará a moeda do resultado;
    """
    desconto = str(float(num * (1 - (porcent/100)))).replace(".",",")
    if moed == '':
        return desconto
    else:
        return moeda(desconto, moed)


def dobro(num, moed=''):
    """
    /Calculo de dobro de um valor
    -- parâm. num: número base que será multiplicado por 2;
    -- parâm. moed: opcional; (deve ser escrita entre ''); opções: 'real', 'dolar', 'euro'; retornará a moeda do resultado;
    """
    dobro = str(float(num * 2)).replace(".",",")
    if moed == '':
        return dobro
    else:
        return moeda(dobro, moed)


def metade(num, moed=''):
    """
    /Calculo de metade de um valor
    -- parâm. num: número base que será dividido por 2;
    -- parâm. moed: opcional; (deve ser escrita entre ''); opções: 'real', 'dolar', 'euro'; retornará a moeda do resultado;
    """
    metade = str(float(num / 2)).replace(".",",")
    if moed == '':
        return metade
    else:
        return moeda(metade, moed)



def moeda(num=0, coin=''):
    """
    /Aplica uma moeda ao valor e retorna o resultado
    -- parâm. num: número base;
    -- parâm. coin: (deve ser escrita entre ''); opções: 'real', 'dolar', 'euro';
    """
    numero = num
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


def resumo(num):
    print("=========================== RESUMO ===========================")
    print(f"O dobro de {num} é {dobro(num, 'real')}")
    print(f"A metade de {num} é {metade(num, 'real')}")
    print(f"{num} sofreu um aumento de 10% e resultou em {aumento(num, 10, 'real')}")
    print(f"{num} ganhou um desconto de 30% e resultou em {desconto(num, 30, 'real')}")
    print(f"{num} em euros -- {moeda(num, 'euro')}")
    print(f"{num} em reais -- {moeda(num, 'real')}")
    print(f"{num} em dolares -- {moeda(num, 'dolar')}")
    print("=============================================================")

    
