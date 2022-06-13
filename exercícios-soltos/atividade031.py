dist = float(input('Digite a distancia da sua viagem(km): '))
if dist <= 200:
    print('valor da sua passagem: R${:.2f}'.format(dist*0.50))
else: print('valor da sua passagem: R${:.2f}'.format(dist*0.45))


#Forma Simples abaixo:
#dist = float(input('distancia da viagem: '))
#preço = dist*0.50 if dist <= 200 else dist*0.45
#print('valor da passagem:', preço)
