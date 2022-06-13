maioresmil = 0
total = 0
maisbarato = ''
valormaisbarato = 0

while True:
    nome = str(input("Produto: ")).lower().strip()
    valor = float(input("Preço: R$"))
    total += valor

    if valor > 1000:
        maioresmil += 1
    if valormaisbarato == 0:
        valormaisbarato = valor
        maisbarato = nome
    if valor < valormaisbarato:
        maisbarato = nome
        valormaisbarato = valor

    continuar = str(input("deseja continuar? ")).lower().strip()
    if continuar == 'nao':
        break
print("====== CARRINHO DE COMPRAS ======")
print(f"Total gasto: R${total}\nProdutos que custam mais de R$1000: {maioresmil}\nProduto mais barato: {maisbarato}")