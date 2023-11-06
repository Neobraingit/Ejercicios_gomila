def fibonacci(n):
    # Inicializamos los dos primeros números de la secuencia
    a, b = 0, 1
    fibonacci_sequence = []

    # Generamos la secuencia de Fibonacci de n elementos
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

# Especifica cuántos elementos deseas en la secuencia de Fibonacci
n = int(input("Ingrese la cantidad de elementos que deseas en la secuencia de Fibonacci: "))

if n <= 0:
    print("La longitud de la secuencia debe ser un número positivo.")
else:
    resultado = fibonacci(n)
    print("Secuencia de Fibonacci de {} elementos:".format(n))
    print(resultado)

        
        
        
  