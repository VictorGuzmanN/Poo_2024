
#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado
numeros = [5, 12, 3, 18, 7, 22, 9, 1]
print("Lista original:")
for num in numeros:
    print(num, end=" ")
print("\n")
def lista_a_string(lista):
    cadena = ""
    for num in lista:
        cadena += str(num) + " "
    return cadena.strip()
string_numeros = lista_a_string(numeros)
print("Lista en forma de string:", string_numeros)
print("\n")
numeros.sort()
print("Lista ordenada:")
for num in numeros:
    print(num, end=" ")
print("\n")
print("Longitud de la lista:", len(numeros))
print("\n")
elemento = int(input("Ingrese un número entero para buscar en la lista: "))
if elemento in numeros:
    print(f"El número {elemento} se encuentra en la lista.")
else:
    print(f"El número {elemento} no se encuentra en la lista.")