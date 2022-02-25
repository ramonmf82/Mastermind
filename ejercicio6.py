#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

def max(num1, num2):

    if num1 > num2:

        return num1

    else:

        return num2

#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(num1, num2, num3):

    return max(num1, max(num2, num3))

#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
# solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
# Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lista):

    resultado = lista[0]

    for i in lista:

        if i > resultado:

            resultado = i

    return resultado

print(max(13,13))

print(max_de_tres(-22,12,12))

print(max_in_list([-7, -4, -27, -27, -28, 4, -9, -27]))