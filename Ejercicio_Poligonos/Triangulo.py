from Poligono import *
from math import *

class Triangulo(Poligono):

    def __init__(self, base, lado2, lado3):

        super().__init__(base)
        self.lado2 = lado2
        self.lado3 = lado3

    def lado2(self):

        return self.lado2

    def lado3(self):

        return self.lado3    

    def es_triangulo(self):

        return self.base + self.lado2 >= self.lado3 and \
               self.base + self.lado3 >= self.lado2 and \
               self.lado2 + self.lado3 >= self.base

    def es_equilatero(self):

        return self.base == self.lado2 == self.lado3

    def es_isosceles(self):

        return self.es_triangulo() and \
               (self.base == self.lado2 != self.lado3 or \
               self.base == self.lado3 != self.lado2 or \
               self.lado2 == self.lado3 != self.base)

    def es_escaleno(self):

        return self.es_triangulo() and not self.es_equilatero() and not self.es_isosceles()

    def es_rectangulo(self):
        
        if self.es_triangulo() and not self.es_equilatero():
            return self.base**2 == self.lado2**2 + self.lado3**2 or \
                   self.lado2**2 == self.lado3**2 + self.base**2 or \
                   self.lado3**2 == self.base**2 + self.lado2**2
        else:
            return False

    def perimetro(self):

        if self.es_triangulo():
            return self.base + self.lado2 + self.lado3 
        else:
            return -1

    def area(self):

        if self.es_triangulo():
            s = self.perimetro() / 2
            area = sqrt(s * (s - self.base) * (s - self.lado2) * (s - self.lado3))
            return area
        else:
            return -1

    def mostrar(self):
        
        print("Datos del Triángulo: ")
        print(f"Lado 1: {self.base}\nLado 2: {self.lado2}\nLado 3: {self.lado3}")
        if not self.es_triangulo():
            print("No es un triángulo")
        else:
            if self.es_equilatero():
                print(f"Perímetro: {self.perimetro()}\nÁrea: {self.area()}\nEs un triángulo equilátero")
            if self.es_isosceles():
                print(f"Perímetro: {self.perimetro()}\nÁrea: {self.area()}\nEs un triángulo isósceles")
            if self.es_escaleno():
                print(f"Perímetro: {self.perimetro()}\nÁrea: {self.area()}\nEs un triángulo escaleno")
            if self.es_rectangulo():
                print("Es un triángulo rectángulo")
