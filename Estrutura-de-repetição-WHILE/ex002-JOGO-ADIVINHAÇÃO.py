import random
import time
time.sleep(1)
print("olá, vou pensar em um numero de 0 a 10 e quero que você tente advinhar")

alea = random.randrange(11)
tries = 0

time.sleep(2.5)
print("la vai..")

time.sleep(1)
resposta = int(input("Pensei! advinha: "))
while  resposta > 10:
    resposta = int(input("eu disse 'um numero de 0 a 10', digite novamente: "))
while resposta != alea:
    tries += 1
    resposta = int(input("errooou.. tenta denovo: "))
if 3 >= tries > 0:
    print("Acertou, Cabron! Pensei mesmo em {}... suas tentativas: {}".format(alea, tries))
if tries > 3:
    print("Foi dificil ein kk mas pensei mesmo em {}...suas tentativas: {}".format(alea, tries))
if tries == 0:
    print("reioreee de primeira ein!! Acertou, pensei mesmo em {}...".format(alea))