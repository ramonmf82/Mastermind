class Persona:

    def __init__(self, nombre, edad, dni):

        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):

        return self.nombre

    def get_edad(self):

        return self.edad

    def get_dni(self):

        return self.dni

    def es_mayor_de_edad(self):

        return self.edad >= 18

    def mostrar(self):

        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")


