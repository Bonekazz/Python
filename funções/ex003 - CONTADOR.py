import time


def contador(inicio, fim, passo):
    if inicio > fim:
        for c in range(inicio, fim - 1, -(passo)):
            print(f"{c} ", end='', flush=True)
            time.sleep(0.5)
    if inicio > fim and passo < 0:
        for c in range(inicio, fim - 1, passo):
            print(f"{c} ", end='', flush=True)
            time.sleep(0.5)
    else:
        for c in range(inicio, fim + 1, passo):
            print(f"{c} ", end='', flush=True)
            time.sleep(0.5)


inicio = int(input("Inicio: "))
fim = int(input("fim: "))
passo = int(input("intervalo: "))
contador(inicio, fim, passo)