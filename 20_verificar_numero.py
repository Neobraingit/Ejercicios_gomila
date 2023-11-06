# Verificar si un número es positivo, negativo o cero.

numero = float(input('Introduce un número: '))

if numero > 0:
    print ('El número {} es positivo.'.format(numero))
elif numero < 0:
    print ('El numero {} es negativo.'.format(numero))
else:
    print ('El numero {} es 0'. format(numero))