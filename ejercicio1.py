#calcular las soluciones de una ecuación de segundo grado dados los coeficientes a, b y c.

from math import *
from random import *

a = uniform(-10, 10)
b = uniform(-10, 10)
c = uniform(-10, 10) 

print(f"Los coeficientes son:\na = {a}\nb = {b}\nc = {c}")

discriminante = b**2 - 4 * a * c 

if discriminante > 0:

    sol1 = (-b + sqrt(discriminante)) / (2 * a)

    sol2 = (-b - sqrt(discriminante)) / (2 * a)

    print(f"El discriminante: {discriminante} es positivo, por tanto existen dos soluciones reales distintas")
    print(f"Las dos soluciones son: {sol1} y {sol2}")

elif discriminante == 0:

    sol = -b/ (2 * a)

    print(f"El discriminante: {discriminante} es nulo, por tanto existe una única solución")
    print(f"La solución es: {sol}")

else:

    print(f"El discriminante: {discriminante} es negativo, por tanto no existen soluciones reales")

print("Fin del programa")
