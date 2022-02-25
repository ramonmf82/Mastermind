from Poligono import *

class Rectangulo(Poligono):

    def __init__(self, base, altura):

        super().__init__(base)
        self.altura = altura

    def altura(self):

        return self.altura

    def perimetro(self):

        return self.base * 2 + self.altura * 2

    def area(self):

        return self.base * self.altura

    def mostrar(self):

        print("Datos del Rectángulo: ")
        print(f"Base: {self.base}\nAltura: {self.altura}")
        print(f"Perímetro: {self.perimetro()}\nÁrea: {self.area()}")