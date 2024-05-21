#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario




numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))


print(f"Números impares entre {numero1} y {numero2}:")


for numero in range(numero1, numero2 + 1):
    if numero % 2 != 0:
        print(numero)
