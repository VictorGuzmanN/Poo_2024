# # Crear instancias de Estudiantes y Docentes
from clases import Estudiantes, Docentes
# estudiante1 = Estudiantes("Ana Torres Guzmán", "Col. Centro 1500", "6181234567", "MECA", "2335678")
# docente1 = Docentes("Daniel Fuentes Loera", "Fracc. D. Arieta 1400", "6183375587", "TT", "123")

# # Demostración de métodos
# estudiante1.reservar()
# estudiante1.entregar()
# docente1.reservar()
# docente1.entregar()


# Ejemplo de uso
estudiante = Estudiantes("Ana Torres Guzman", 20, 6181234567, "MECA", 235678)
print(f"Nombre: {estudiante.nombre}")
print(f"Edad: {estudiante.edad}")
print(f"Teléfono: {estudiante.tel}")
print(f"Carrera: {estudiante.carrera}")
print(f"Matrícula: {estudiante.matricula}")

docente = Docentes("Daniel Fuentes Loera", 40, 6183335678, "TI", 123)
print(f"Nombre: {docente.nombre}")
print(f"Edad: {docente.edad}")
print(f"Teléfono: {docente.tel}")
print(f"Modalidad: {docente.modalidad}")
print(f"Número de empleado: {docente.num_empleado}")