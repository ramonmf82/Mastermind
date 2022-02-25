#Definir una función que calcule la longitud de una lista o una cadena dada. 
#(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(cadena):

    contador = 0

    for i in cadena:

        contador += 1

    return contador 

#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(caracter):

    caracter = caracter.lower()

    return caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u'

print(es_vocal('u'))

print(longitud('hola hola'))