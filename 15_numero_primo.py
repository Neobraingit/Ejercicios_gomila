# Comprobar si un número es primo.
numero = int(input('Introduce un número: '))
if numero % numero == 1 and numero % 1 == 1:
    print ('Es un número primo')
else:
    print ('No es un número primo')