#En este ejercicio se da la opción de resolver varios tipos de problemas. 
#Para ello he creado en módulo funciones_ej2 con unas cuantas funciones que se emplean 
#varias veces durante la ejecución del programa

from math import *
from funciones_ej2 import *

while True:
    
    barras()
    opa()   #area circunferencia
    opb()   #volumen esfera
    opc()   #area triangulo
    opd()   #interés compuesto
    ope()   #distancia entre dos puntos
    opf()   #ecuación segundo grado
    barras()

    opcion = input("\nEliga la opción que desee: ")

    if opcion == 'a' or opcion == 'b' or opcion == 'c' or opcion == 'd' or opcion == 'e' or opcion == 'f':
        break

    else:

        print("\nOpción incorrecta. Vuelva a elegir\n")

if opcion == 'a':

    barras()
    opa()
    barras()
    
    radio = int(input("\nIntroduzca el radio de la circunferencia: "))
    
    area = round(pi * radio**2, 2)

    print(f"\nEl área de una circunferencia de radio {radio} unidades es de {area} unidades cuadradas")
    
if opcion == 'b':

    barras()
    opb()
    barras()

    radio = int(input("\nIntroduzca el radio de la esfera: "))

    volumen = round((4 * pi * radio**3) / 3, 2)

    print(f"\nEl volumen de una esfera de radio {radio} unidades es de {volumen} unidades cúbicas")

if opcion == 'c':

    barras()
    opc()
    barras()

    base = int(input("\nIntroduzca la base: "))
    altura = int(input("\nIntroduzca la altura: "))

    area = round(base * altura / 2, 2)

    print(f"\nEl área de un triángulo de base {base} unidades y altura {altura} unidades es de {area} unidades cuadradas")

if opcion == 'd':

    barras()
    opd()
    barras()

    ci = int(input("\nIntroduzca la cantidad inicial: "))
    r = int(input("\nIntroduzca el interés: "))
    t = int(input("\nIntroduzca los años: "))

    cantidad = round(ci * (1 + (r /100))**t, 2)

    print(f"\nLa cantidad final es de {cantidad} euros")

if opcion == 'e':
    
    barras()
    ope()
    barras()

    print("\nIntroduzca las coordenadas del primer punto:")
    x1 = int(input("\nCoordenada X: "))
    y1 = int(input("\nCoordenada Y: "))

    print("\nIntroduzca las coordenadas del segundo punto:")
    x2 = int(input("\nCoordenada X: "))
    y2 = int(input("\nCoordenada Y: "))

    distancia = round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

    print(f"\nCoordenadas del primer punto: ({x1}, {y1})")
    print(f"\nCoordenadas del segundo punto: ({x2}, {y2})")
    print(f"\nLa distancia entre ellos es: {distancia} unidades")

if opcion == 'f':

    barras()
    opf()
    barras()

    print("\nIntroduzca los coeficientes:")
    a = int(input("\nCoeficiente a: "))
    b = int(input("\nCoeficiente b: "))
    c = int(input("\nCoeficiente c: "))

    print(f"\nLos coeficientes son:\na = {a}\nb = {b}\nc = {c}")

    discriminante = b**2 - 4 * a * c 

    if discriminante > 0:

        sol1 = (-b + sqrt(discriminante)) / (2 * a)

        sol2 = (-b - sqrt(discriminante)) / (2 * a)

        print(f"\nEl discriminante vale {discriminante}. Es positivo, por tanto existen dos soluciones reales distintas")
        print(f"\nLas dos soluciones son: {sol1} y {sol2}")

    elif discriminante == 0:

        sol = -b/ (2 * a)

        print(f"\nEl discriminante vale {discriminante}. Es nulo, por tanto existe una única solución")
        print(f"\nLa solución es: {sol}")

    else:

        print(f"\nEl discriminante vale {discriminante}. Es negativo, por tanto no existen soluciones reales")

print("\n\nFin del programa")