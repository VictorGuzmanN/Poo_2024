class Persona:
    def __init__(self, nombre, edad, DNI)   -> None:
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI


    def presentarse(self):
        print(f"Hola! Me llamo {self.nombre} y tengo {self.edad}")

oscar = Persona("Oscar", 23, "12345678")
oscar.presentarse()
print(oscar.DNI)

class trabajador(Persona):
    pass



trabajador = trabajador ("Juan", 33, "16354")
trabajador.presentarse



