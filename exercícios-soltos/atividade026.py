palavra = input('digite qualquer coisa: ').strip()
texto = palavra.lower()
print('"{}" tem {} "A"'.format(palavra, texto.count('a')))
print('''A primeira letra "a" aparece na posição {}
A ultima letra "a" aparece na posição {}'''.format(texto.find('a')+1, texto.rfind('a')+1-texto.count(' ')))
