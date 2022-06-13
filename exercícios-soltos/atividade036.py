valorcasa = float(input('Valor da casa: '))
salario = float(input('Seu salario: '))
parcelas = float(input('Quer parcelar em quantas vezes? '))
mensalidade = valorcasa/parcelas

if mensalidade > (30*salario/100):
    print('Voce nao tem os requisitos para receber este emprestimo')
else:
    print('Emprestimo confirmado')
