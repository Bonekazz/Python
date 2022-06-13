import time
awnser = 'sim'
while awnser == 'sim':
    print("You Dead...")
    awnser = str(input("Deseja continuar? [sim/nao]")).lower()
    time.sleep(1)
    print("loading...")
    time.sleep(1)
print("You quit the game.")
