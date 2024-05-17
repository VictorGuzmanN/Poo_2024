# Ciclo for estructura iteractiva que se ejecuta x veces

# Sintaxis
# for variable in elemento iterable (lista, rango, etc)
# bloque de instrucciones

# ejemplo 1
# Crear un programa que imprima en pantalla 5 veces el @

contador=1

for contador in range(1,6):
    print("@")

#Ejemplo 2
#Crear un programa que imprima los numeros de 1 al 5 y los sume y al final
#imprima la suma
contador=1
suma=0

for contador in range(1,6):
    print(contador)
    suma+=contador

print(f"La suma es: {suma}")


# ejemplo 3
# crear un programa que imprima la tabla de multiplicar que el usuario desee
tabla=int(input("Ingresa un numero para calcular la tabla de multiplicar: "))
i=1

multi=0

for i in range(1,11):
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")