# Variable global
NUMERO_GLOBAL = 10

def funcion_con_variables():
    # Variable local
    numero_local = 5

    print("Dentro de la función:")
    print("Variable global:", NUMERO_GLOBAL)
    print("Variable local:", numero_local)

    # Acceder a la variable global dentro de la función
    NUMERO_GLOBAL_MODIFICADO = NUMERO_GLOBAL + 5
    print("Variable global modificada:", NUMERO_GLOBAL_MODIFICADO)

    # Modificar la variable global dentro de la función
    global NUMERO_GLOBAL
    NUMERO_GLOBAL = 20
    print("Variable global modificada:", NUMERO_GLOBAL)

# Llamada a la función
funcion_con_variables()

print("\nFuera de la función:")
print("Variable global:", NUMERO_GLOBAL)

# Intento de acceder a la variable local fuera de la función (generará un error)
# print("Variable local:", numero_local)