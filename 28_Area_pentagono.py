# Calcular el área de un pentágono.

lado = float(input('Define el largo del lado: '))
perimetro = lado * 5
apotema = float(input('Introduce la apotema del polígono: '))

area = (perimetro * apotema) / 2
print ('El área del pentágono es: {} '.format(area))