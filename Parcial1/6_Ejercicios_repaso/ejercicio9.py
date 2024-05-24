#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

# Inicializamos una lista para almacenar los números
numeros = []

while True:
    try:
        # Solicitamos al usuario un número
        numero = float(input("Introduce un número (111 para salir): "))
        
        # Si el número es 111, salimos del bucle
        if numero == 111:
            break
        
        # Agregamos el número a la lista
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Mostramos los números ingresados
print("Números ingresados:", numeros)
