from Poligono import *

class Cuadrado(Poligono):

    def __init__(self, base):

        super().__init__(base)

    def perimetro(self):

        return self.base * 4

    def area(self):

        return self.base**2

    def mostrar(self):

        print("Datos del Cuadrado: ")
        print(f"Lado: {self.base}\nPerimetro: {self.perimetro()}\nÁrea: {self.area()}")