import time

while True:
    numero = int(input("Digite um valor: "))
    if numero < 0:
        break
    else:
        time.sleep(1)
        print(f"======= Tabuada do {numero} =======")
        for c in range(0,11):
            print(f"{numero} X {c}: {(numero*c)}")
        print("=====================")

time.sleep(1)
print("fim do programa...")
time.sleep(1.2)
