
# Escribir un programa que añada valores a una lista mientras que su 
# longitud sea menor a 120, y luego mostrar la lista
# usar un While y for
lista = []
while len(lista) < 120:
    valor = input(f"Ingrese un valor (la lista tiene {len(lista)} elementos): ")
    lista.append(valor)
print("Lista completa:")
for elemento in lista:
    print(elemento)