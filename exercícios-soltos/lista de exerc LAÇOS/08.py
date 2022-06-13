frase = str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
tudojunto = ''.join(palavras)
let = ''
for c in range(len(tudojunto) - 1, -1, -1):
    let = let + tudojunto[c]
if let == tudojunto:
    print('esta frase é um palindromo')
    print(tudojunto, '-', let)
else:
    print('esta frase nao é um palindromo')
    print(tudojunto, '-', let)



    
