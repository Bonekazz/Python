ret1 = float(input('reta1: '))
ret2 = float(input('reta2: '))
ret3 = float(input('reta3: '))
result = True
if ret1 < (ret2 - ret3) and ret1 > (ret2 + ret3):
    result = False
if ret2 < (ret1 - ret3) and ret2 > (ret1 + ret3):
    result = False
if ret3 < (ret2 - ret1) and ret3 > (ret2 + ret1):
    result = False
if result == True:
    print('As retas formam sim um triangulo.')
else:
    print('As retas nao formam um triangulo')
