print('Digite a Altura e o Comprimento da parede que deseja pintar, e direi sua área e a quantidade necessária de tinta para pinta-la:')
a = float(input('Altura: '))
c = float(input('Comprimento: '))
area = a*c
l = area/2
print('A área da parede equivale a {:.1f} m², para pinta-la será necessário {:.1f} L de tinta.'.format(area, l))


