# Manejo de errores es la forma que tienen los lenguajes de programacion
# para evitar que sucedan errores en tiempo de ejecucion

#Ejemplo 1 Error cuando una variable no se genera
# try:
#     nombre=input("Dame el nombre: ")
#     if len(nombre)>1:
#         nombre_usuario="El nombre es: "+nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuario")


#Ejemplo 2 Cuando se solicita un numero y se introduce una letra
# try:
#     numero=int(input("Dame un numero: "))

#     if numero>0:
#         print("Soy un numero entero positivo")
#     else:
#         print("Soy un numero entero negtivo")
# except:
#     ("No se puede convertir un caraxter no numerico a numero")
# else:
#     print("Todo se ejecuto sin errores")

#Ejemplo numero 3 Cuando se generan multiples excepciones
try:
    numero=int(input("Dame un numero: "))

    print("El cuadrado es:")+str (numero*numero)

except ValueError:
    print("Debes de introducir un numero, no se puede convertir un numero que no sea numerico")
except TypeError:
    print("No es posible convertir a numero entero")

else:
    print("Todo se ejecuto correctamente")

finally:
    print("Listo, se termino")
