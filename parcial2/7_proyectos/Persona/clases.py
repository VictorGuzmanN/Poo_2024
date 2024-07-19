# class personas:
#     def _init_(self, nombre, edad, tel):
#         self.nombre = nombre
#         self.edad = edad
#         self.tel = tel

#     def reservar(self):
#         print(f"{self.nombre} ha reservado un libro.")

#     def entregar(self):
#         print(f"{self.nombre} ha entregado un libro.")


# class Estudiantes(personas):
#     def _init_(self, nombre, direccion, tel, carrera, matricula):
#         super()._init_(nombre, direccion, tel)
#         self.carrera = carrera
#         self.matricula = matricula


# class Docentes(personas):
#     def _init_(self, nombre, direccion, tel, modalidad, num_empleado):
#         super()._init_(nombre, direccion, tel)
#         self.modalidad = modalidad
#         self.num_empleado = num_empleado


class Personas:
    def __init__(self, nombre: str, edad: int, tel: int):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

class Estudiantes(Personas):
    def __init__(self, nombre: str, edad: int, tel: int, carrera: str, matricula: int):
        super().__init__(nombre, edad, tel)
        self.carrera = carrera
        self.matricula = matricula

class Docentes(Personas):
    def __init__(self, nombre: str, edad: int, tel: int, modalidad: str, num_empleado: int):
        super().__init__(nombre, edad, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado

