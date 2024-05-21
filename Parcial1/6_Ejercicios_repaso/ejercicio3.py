# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

# Mostrar los cuadrados de los 60 primeros números naturales con while
contador = 1
while contador <= 60:
    cuadrado = contador ** 2
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1



# Mostrar los cuadrados de los 60 primeros números naturales usando for
for contador in range(1, 61):
    cuadrado = contador ** 2
    print(f"El cuadrado de {contador} es {cuadrado}")
