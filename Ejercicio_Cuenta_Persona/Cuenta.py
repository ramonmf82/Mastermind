from Persona import *

class Cuenta():

    def __init__(self, persona, cantidad):

        self.persona = persona
        self.cantidad = cantidad
    
    def get_cantidad(self):

        return self.cantidad

    def ingresar(self, cantidad):

        if cantidad > 0:

            self.cantidad += cantidad
    
    def retirar(self, cantidad):

        if cantidad > 0:
            
            self.cantidad -= cantidad

    def mostrar(self):

        print(f"Nombre: {self.persona.nombre}\nEdad: {self.persona.edad}\nDNI: {self.persona.dni}\nCantidad: {self.cantidad}")