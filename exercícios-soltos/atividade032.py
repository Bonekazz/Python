ano = int(input('digite em que estamos e direi se é bissexto ou nao: '))
result = ano%4
if result == 0:
    print('{} é bissexto'.format(ano))
else:
    print('{} nao é bissexto'.format(ano))
