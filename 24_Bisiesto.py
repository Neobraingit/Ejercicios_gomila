# Determinar si un año es bisiesto.

año = int(input('Introduce un año: '))

if año % 4 == 0 :
    print ('{} es bisiesto '.format(año))
else:
    print ('{} no es bisiesto'.format(año))