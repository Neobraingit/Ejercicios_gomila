
cadena = input('Introduce una cadena de texto: ')
contador = 0
longitud = []
for i in cadena:
    if i != ' ':
        contador += 1
        longitud.append(i)
print ('La cadena tiene {} letras.'.format(contador))
print (longitud)

