# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo(valor):
    """
    Función que imprime el tipo de dato de una variable.
    
    Args:
        valor (any): La variable cuyo tipo de dato se va a imprimir.
    """
    print(f"El tipo de dato de '{valor}' es: {type(valor)}")

def main():
    # Crear las 4 variables
    mi_lista = [1, 2, 3, 4, 5]
    mi_cadena = "Hola, mundo!"
    mi_entero = 42
    mi_logico = True

    # Imprimir el tipo de cada variable
    imprimir_tipo(mi_lista)
    imprimir_tipo(mi_cadena)
    imprimir_tipo(mi_entero)
    imprimir_tipo(mi_logico)

if __name__ == "__main__":
    main()