string = 'Me llamo Marcos Carmona García'
print (string)
palabra= input('Introduce la palabra a eliminar: ')
indice = string.find(palabra)
substring = string [:indice] + string [indice + len(palabra): ]
print (substring)

