#Concatenar cadenas de caracteres con contenido de variables.

nombre="Jacqueline Quezada Robles"
especialidad="Area de Desarrollo de SW Multiplataforma"
carrera="Ingeniero en Gestión y Desarrollo de Software"

#1er forma de concatenar 
print("Mi nombre es: "+nombre+" estoy en la especialidad de: "+especialidad+", en la carrera de: "+carrera)

print("\n")

#2da forma de concatenar 
print("Mi nombre es: ",nombre," estoy en la especialidad de: ",especialidad,", en la carrera de: ",carrera)

#3er forma de concatenar COMUN EN PYTHON
print(f"Mi nombre es: {nombre} estoy en la especialidad de: {especialidad}, en la carrera de: {carrera}")

print("\n")

#4ta forma de concatenar COMUN EN PYTHON
print("Mi nombre es: {}, estoy en la especialidad de: {}, en la carrera de: {}".
format (nombre,especialidad,carrera))

print("\n")

#5ta forma de concatenar COMUN EN PYTHON
print("Mi nombre es: '+nombre+' estoy en la especialidad de: '+especialidad+', en la carrera de: '+carrera")

print("\n")