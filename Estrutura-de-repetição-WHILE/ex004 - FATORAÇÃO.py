num = int(input("Digite um numero e irei mostrar seu fatorial: "))

result = 0
ultimo = num

for c in range(num, 1, -1):
    print(c, end=" x ")
    if c == num:
        ultimo = ultimo
    else:
        result = (c * ultimo)
        ultimo = result
if num == 0:
    print("0 = 1") 
else:  
    print("1 = {}".format(ultimo))

#or import math and change 'result' for math.factorial(num). Its more simple