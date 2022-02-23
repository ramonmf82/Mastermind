#Mastermind

import random

def pedir_numero():

    while True:

        numero = int(input("Introduce un numero de 4 cifras: "))

        if numero < 1000 or numero > 9999:

            print("Incorrecto")

        else:

            return numero
    
contador = 0    #contador de intentos

numero_oculto = random.randint(1000, 9999) 

millares_oculto = numero_oculto // 1000
centenas_oculto = (numero_oculto // 100) % 10
decenas_oculto = (numero_oculto // 10) % 10
unidades_oculto = numero_oculto % 10

while True:

    tu_numero = pedir_numero()

    contador += 1

    millares_tu = tu_numero // 1000
    centenas_tu = (tu_numero // 100) % 10
    decenas_tu = (tu_numero // 10) % 10
    unidades_tu = tu_numero % 10

    print(tu_numero)

    if millares_oculto == millares_tu:

        print('*', end = '')

    else:

        print(' ', end = '')

    if centenas_oculto == centenas_tu:

        print('*', end = '')

    else:

        print(' ', end = '')

    if decenas_oculto == decenas_tu:

        print('*', end = '')

    else:

        print(' ', end = '')

    if unidades_oculto == unidades_tu:

        print('*')

    else:

        print(' ')

    if tu_numero == numero_oculto:

        print("¡¡¡Victoria!!!")
        print(f"Has usado {contador} intentos")

        break