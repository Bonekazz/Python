cidade = input('Digite o nome da sua cidade: ')
nometodo = cidade.split()
if 'Santo' in nometodo[0]:
    print('Sua cidade começa com "Santo" vc ganhou um cupom!')
elif 'Santo' not in nometodo[0]:
    print('seu pedido foi registrado')
