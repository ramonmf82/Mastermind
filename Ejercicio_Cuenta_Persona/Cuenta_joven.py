from glob import escape
from Cuenta import *

class Cuenta_joven(Cuenta):

    def __init__(self, persona, cantidad, bonificacion):

        super().__init__(persona,cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):

        return self.bonificacion

    def es_titular_valido(self):

        return self.persona.es_mayor_de_edad() and self.persona.edad < 25

    def retirar(self, cantidad):

        if self.es_titular_valido() and cantidad >= 0:

            self.persona.cantidad -= cantidad

    def mostrar(self):

        print("Se trata de una cuenta joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}")

