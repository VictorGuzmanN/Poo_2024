# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

# Crear la lista y el diccionario
peliculas = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

generos = {
    "ACCION": peliculas[0][0],
    "TERROR": peliculas[0][1],
    "DEPORTES": peliculas[0][2],
    "ACCION": peliculas[1][0],
    "TERROR": peliculas[1][1],
    "DEPORTES": peliculas[1][2],
    "ACCION": peliculas[2][0],
    "TERROR": peliculas[2][1],
    "DEPORTES": peliculas[2][2]
}

# Imprimir la información
print("LISTA DE PELÍCULAS:")
for fila in peliculas:
    print(f"ACCION: {fila[0]}, TERROR: {fila[1]}, DEPORTES: {fila[2]}")

print("\nDICCIONARIO DE PELÍCULAS:")
for genero, pelicula in generos.items():
    print(f"{genero}: {pelicula}")