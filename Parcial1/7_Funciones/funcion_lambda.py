# Función lambda para cuadrado de un número
cuadrado = lambda x: x ** 2

# Llamada a la función lambda
print(cuadrado(5))  # Output: 25

# Función lambda para sumar dos números
suma = lambda a, b: a + b

# Llamada a la función lambda
print(suma(3, 4))  # Output: 7

# Uso de funciones lambda con otras funciones
numeros = [1, 2, 3, 4, 5]

# Filtrar números pares usando una función lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]

# Multiplicar cada número por 2 usando una función lambda
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Output: [2, 4, 6, 8, 10]