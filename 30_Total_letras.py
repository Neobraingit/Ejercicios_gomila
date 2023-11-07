cadena = input('Introduce un cadena de texto: ')
contador = 0

for i in cadena:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        contador += 1
print ('La cadena tiene {} vocales.'.format(contador))
