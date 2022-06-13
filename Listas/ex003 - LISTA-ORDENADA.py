list = []
menor = 0
for c in range(0, 5):
    num = int(input("Dgite um valor: "))
    if c == 0:
        menor = num
        list.insert(0, menor)
    else: 
        if num < menor:
            menor = num
            list.insert(0, menor)
        else:
            list.append(num)
print(list)