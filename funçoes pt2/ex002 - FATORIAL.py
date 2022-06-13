def fatorial(num, show=False):
    """
    / A função irá calcular o fatorial de um número dado.
    - parâmetro 'num': deve ser um numero inteiro natural(positivo). Será utilizado para realizar o calculo fatorial.
    - parãmetro 'show': se for True, a função irá printar todo o calculo. Se for False, o padrão, a função irá printar apenas o 'num' e seu fatorial.
    """
    fat = 0
    if num == 0:
        return f"O fatorial de 0 será sempre 1"
    else:
        for c in range(num, 0, -1):
            if c == num:
                fat = num
                if show == True:
                    print(c, end=' x ')
            elif c == 1:
                if show == True:
                    print(c, end=' = ')
            else: 
                fat *= c
                if show == True:
                    print(c, end=' x ')
        if show == True:
            return fat
        else:
            return f"O fatorial de {num} é igual a {fat}"


fat = int(input("Digite um numero para saber o seu fatorial: "))
while True:
    if fat < 0:
        fat = int(input("O numero não pode ser negativo. Digite um numero natural para saber o seu fatorial: "))
    else: 
        break
seq = str(input("Deseja ver toda a sequencia? ")).strip().lower()
while True:
    if seq == 'sim' or seq == 'nao' or seq == '':
        break
    else:
        seq = str(input("Resposta inválida. Deseja ver toda a sequencia? ")).strip().lower()
if seq == 'sim':
    seq = True
else:
    seq = False
print(fatorial(fat, seq))
help(fatorial)


