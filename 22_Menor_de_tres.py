
# Encontrar el menor de tres números.

num1 = float(input('Introduce un número: ' ))
num2 = float(input('Introduce otro número: '))
num3 = float(input('Introduce un tercer número: '))

if num1 <= num2 and num1 <= num3:
    print ('{} es menor'.format(num1))
elif num2 <= num1 and num2 <= num3:
    print ('{} es menor'.format(num2))
else:
    print ('{} es menor'.format(num3))