# Una funcion es un conjunto de instrucciones  agrupadas bajo un 
# nombre en particular coo un programa mas pequeño que cumple
# una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla 
# es decir mandarla llamar

# sintaxis

# def NombreDeMiFuncion(parametros):
#     bloque o conjunto de instrucciones


# NombreDeMiFuncion

# Las funciones pueden ser de  4 tipos
# 1. Funcion que no recibe parametros y no regresa valor 
# 2. Funcion que no recibe parametros y regresa valor 
# 3. Funcion que recibe parametros y no regresa valor 
# # 4. Funcion que recibe parametros y regresa valor 

# #1. Funcion que no recibe parametros y no regresa valor 
# def sumaNumeros1():
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 1:"))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")

#     sumaNumeros1()


# # 2. Funcion que no recibe parametros y regresa valor 
# # def sumaNumeros2():
# #     n1=int(input("Numero # 1:"))
# #     n2=int(input("Numero # 1:"))
# #     suma=n1+n2
# #     return f"{n1}+{n2}={suma}"

# # print(sumaNumeros2)


# # 3. Funcion que recibe parametros y no regresa valor 
# # def sumaNumeros3(n1,n2):
# #     suma=n1+n2
# #     print (f"{n1}+{n2}={suma}")

# # n1=int(input("Numero # 1:"))
# # n2=int(input("Numero # 2:"))    

# # sumaNumeros3(34,23)





# # # 4. Funcion que recibe parametros y regresa valor 
# # def sumaNumeros4(n1,n2):
# #     suma=n1+n2
# #     return f"{n1}+{n2}={suma}"

# # n1=int(input("Numero # 1:"))
# # n2=int(input("Numero # 2:"))    

# # print(sumaNumeros4(n1,n2))


# # crear un programa que solicite a traves de una funcion la siguiente informacion: 
# # nombre del paciente, edad, estatura, tipo de sangre (utilizar los cuatro tipos de  funciones)



# def calcular_imc(peso, estatura):
#     """
#     Función que recibe parámetros y regresa valor.

#     """
#     # Convertir la estatura de centímetros a metros
#     estatura_metros = float(estatura) / 100
#     # Calcular el IMC
#     imc = peso / (estatura_metros ** 2)
#     return imc

# def mostrar_resultado(imc):
#     """
#     Función que recibe parámetros y no regresa valor.

#     """
#     if imc < 18.5:
#         print("El paciente tiene bajo peso.")
#     elif 18.5 <= imc < 24.9:
#         print("El paciente tiene un peso saludable.")
#     elif 25 <= imc < 29.9:
#         print("El paciente tiene sobrepeso.")
#     else:
#         print("El paciente tiene obesidad.")

# # Solicitar información al usuario
# solicitar_informacion()

# peso_paciente = float(input("Ingrese el peso del paciente (en kilogramos): "))
# imc_paciente = calcular_imc(peso_paciente, estatura)
# mostrar_resultado(imc_paciente)




