# Representación de las clases en Python

class Personal:
    def __init__(self, nombre: str, apellido: str, cargo: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

class Mascota:
    def __init__(self, nombre: str, tipo_animal: str):
        self.nombre = nombre
        self.tipo_animal = tipo_animal

class Animales:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre)
        self.raza = raza

class Gato(Animales):
    def __init__(self, nombre: str, color: str):
        super().__init__(nombre)
        self.color = color

class Usuario:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

class Admin(Usuario):
    def __init__(self, nombre: str, direccion: str, telefono: str):
        super().__init__(nombre, direccion)
        self.telefono = telefono

class Menu:
    def __init__(self, nombre: str):
        self.nombre = nombre

# ...and so on for each class.
