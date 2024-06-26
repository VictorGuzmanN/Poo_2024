# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

# Crear una lista vacía
mi_lista = []

# Función para verificar si la lista está vacía y, en caso afirmativo, llenarla
def llenar_lista():
    while True:
        if not mi_lista:
            print("La lista está vacía. Agrega palabras o frases hasta que lo consideres conveniente.")
            while True:
                entrada = input("Ingresa una palabra o frase (o 'salir' para terminar): ")
                if entrada.lower() == "salir":
                    break
                mi_lista.append(entrada)
        else:
            break

# Llamar a la función para verificar y llenar la lista
llenar_lista()

# Imprimir el contenido de la lista en mayúsculas
print("\nContenido de la lista en mayúsculas:")
for elemento in mi_lista:
    print(elemento.upper())