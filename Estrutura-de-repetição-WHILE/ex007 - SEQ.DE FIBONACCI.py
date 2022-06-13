import time

n1 = 0
n2 = 0
n3 = 0

resposta = int(input("Quantos termos vc quer ver: "))
while resposta != 0:
    for c in range(0, resposta):
        if c == 0:
            n3 = c
            print(n3, end=", ")
            n1 = 0
        elif c == 1:
            n3 = c
            print(n3, end=", ")
            n2 = 1
        else:
            n3 = n1 + n2
            print(n3, end=", ")
            n1 = n2
            n2 = n3
    resposta = int(input("Quantos termos vc quer ver agora? "))

time.sleep(1.5)
print("fim do programa...")
time.sleep(1)

 
    
    
    
    
    
