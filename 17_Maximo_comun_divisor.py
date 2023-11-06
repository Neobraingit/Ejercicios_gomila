# Encontrar el máximo común divisor (MCD) de dos números.

import math
n = int(input('Introduce un número: '))
n2 = int(input('introduce otro número'))

mcd = math.gcd(n, n2)

print ('El MCD de los números {} y {} es: {}'.format(n, n2, mcd))
