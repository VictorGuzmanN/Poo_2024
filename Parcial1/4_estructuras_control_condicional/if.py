#Existe una esctructura de condicion llamada "if" la cual evalua una condicion 
#para encontrar en valor "TRUE" y si se cumple la condicion se ejecuta la linea o lineas de codigo


#Tienes 4 variantes de "if"



# #Ejemplo if simple
# color=input("Ingresa un color")

# if color=="rojo":
#     print("Soy el color: rojo")


# #Ejemplo if compuesto
# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color: rojo")
# else:
#     print("No soy el color rojo, soy otro diferente")


# #Ejemplo if anidado
# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color: rojo")
#     if color!="Rojo":
#         print("No soy el color rojo")
# else:
#     print("No soy el color rojo, soy otro diferente")


#Ejemplo if y elif
# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color: rojo")
# elif color=="amarillo":
#     print("Soy el color amarillo")
# elif color=="azul":
#     print("Soy el color azul ")
# else
#     print("No soy ningun color de los anteriores")



#Crear un programa que solicite el numero de la semana e imprima
#en pantalla el dia que le corresponde

numero=input("Ingrese el numero de la semana a buscar: ")
if numero=="1":
    print("Lunes")

if numero=="2":
    print("Martes")

if numero=="3":
    print("Miercoles")

if numero=="4":
    print("Jueves")

if numero=="5":
    print("Viernes")

if numero=="6":
    print("Sabado")

if numero=="7":
    print("Domingo")

else:
    print("No corresponde a ningun dia de la semana, por favor verifique")