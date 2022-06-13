a1 = int(input("digite o pirmeiro termo: "))
ultimovalor = a1
r = int(input("digite a razao: "))
print("(", a1, end=' - ')
for c in range(1, 10):
    ultimovalor = ultimovalor + r
    x = 0
    x = x + ultimovalor
    print(x, end=' - ')
print(")")


