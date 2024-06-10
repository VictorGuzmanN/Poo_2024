# List (Array)
# Son colecciones o conjunto de datos/valores bajo 
# un mismo nombre, para acceder a los valores 
# se hace con un índice numérico

# Nota: sus valores si son modificables

# La lista es una colección ordenada y modificable. Permite miembros 
# duplicados.

#Ejemplo 1. Crear una lista con valores numericos enteros e imprimir la lista.


# numeros=[23,34]
# print(numeros)

# #Recorrer la lista con un for

# for i in numeros:
#     print(i)

# #Recorrer la lista co un while

# i=0
# while i<len(numeros):
#     print(numeros[1]) 
#     i+=1

#Ejemplo 4. Crear una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia 
#en lista E indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

# palabras=["hola","2024","10.23","True"]

# palabras_buscar=input("Ingresa la palabra a buscar: ")


# noencontro=True
# # for i in palabras:
# #     if palabras_buscar==i:
# #         print(f"Encontre la palabra {palabras_buscar} en la posicion: {palabras.index(i)}.")
# #         noencontro=False

# i=0
# while i<len(palabras):
#     if palabras_buscar==palabras[i]:
#     print(f"Encontre la palabra{palabras_buscar}")

# if noencontro:
#     print(f"No se encontro la palabra dentro de la lista")

#EJEMPLO 3 litas multinilinea o multidimensional (matriz) para crear una agenda telefonica

# agenda=[
#     ["Carlos",6181234563],
#     ["Fernando",6182349870],
#     ["Matias",6691112233],
#     ["Juan Polainas",6182332345]
# ]

# print(agenda)

# for i in agenda:
#     print (f"{agenda.index(i)+1}.-(i)")



# Ejemplo 4 Crear un programa que permita gestionar (Administrar) peliculas, colocar
# un menu de opciones para agregar, remover, consultar peliculas
# notas
# utilizar funciones y mandar llamar desde otro archivo
# utilizar listas para almacenar los nombres de peliculas

def insertarPeliculas():
    pelicula=input("Ingresa la pelicula: ")
    peliculas.append(pelicula)
    espereTecla()



def eliminarPeliculas():
    pelicula=input("Ingresa la pelicula a eliminar: ")
    peliculas.remove(pelicula)
    espereTecla()




peliculas=[]

print("\n\t..::: CINEPOLIS CLONADO :::... \n 1.- Agregar \n 2.- Eliminar \n 3.-Consultar \n 4.- Modificar \n 5.- SALIR ")
opcion=input("\t Elige una opcion: ").upper()

if opcion=="1" or opcion=="AGREGAR":
    insertarPeliculas


if opcion=="2" or opcion=="ELIMINAR":
    eliminarPeliculas