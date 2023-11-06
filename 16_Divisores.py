# Encontrar los divisores de un número.

numero = int(input('Introduce un número: '))
divisores = []
for i in range(1, numero + 1):
    if numero & i == 0:
        divisores.append(i)
print ('Los divisores de {} son: {}'.format(numero, divisores))
        


        
    
    