# Crear un programa que solicite la calificacion de 15 alumnos e 
# imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
reprobados = 0

for i in range(1, 16):
    try:
        calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
        if calificacion >= 6:
            aprobados += 1
        else:
            reprobados += 1
    except ValueError:
        print("Por favor, ingrese una calificación válida.")

# Mostramos los resultados
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
