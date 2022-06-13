while True:
    exp = str(input("Digite sua expressão matematica(deve ter parenteses): "))
    parenteses = []
    for c in exp:
        if c == '(':
            parenteses.append('(')
        elif c == ')':
            if len(parenteses) > 0:
                parenteses.pop()
            else:
                parenteses.append(')')
    if len(parenteses) == 0:
        break
    else:
        print("="*50)
        print("Talvez tenha esquecido um parentes aberto.")
        print("="*50)

print("Expressão salva. Au revoir...")
    


  

