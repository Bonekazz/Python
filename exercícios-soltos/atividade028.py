import random
print('Olá, vou pensar em um numero de 0 a 10 e quero ver se voce consegue advinhar...')
alea = random.randrange(11)
num = int(input('Pensei, pode advinhar: '))
if num == alea:
    print('krai tu acertou!')
elif num >10:
    print('eu disse "entre 0 e 10"')
else: 
    print('wrong anwser dude, pensei em {}'.format(alea))



