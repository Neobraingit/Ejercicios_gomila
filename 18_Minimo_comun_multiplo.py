
# Encontrar el mínimo común múltiplo (LCM) de dos números.

import math

n = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))

# MCD
mcd = math.gcd(n, n2)

# MCM
mdm = mcd / n * n2

print (mdm)