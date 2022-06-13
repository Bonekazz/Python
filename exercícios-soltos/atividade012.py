print('digite o preço de um produto e mostrarei seu valor com 30% de desconto')
vp = float(input('Valor do produto: '))
vcd = vp-(vp*30/100)
print('Preço do produto: R${:.2f}\nValor com desconto: R${:.2f}'.format(vp, vcd))
