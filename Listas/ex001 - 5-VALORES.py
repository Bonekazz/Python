list = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    list.append(num)

print(f"O maior número digitado foi {max(list)}, ele está na posição {list.index(max(list)) + 1}")

print(f"O menor valor digitado foi {min(list)}, ele está na posição {list.index(min(list)) + 1}")
