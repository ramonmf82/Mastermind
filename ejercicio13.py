#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

from ejercicio7 import longitud 

def mas_larga(lista):

    resultado = 0
    final = ''

    for palabra in lista:

        contador = 0

        for letra in palabra:

            contador += 1

        if contador > resultado:

            resultado = contador
            final = palabra

    return final

#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y 
#devuelva las palabras que tengan mas de n caracteres.
#Vamos a usar la función longitud() que hemos creado en el ejercicio7

def filtrar_palabras(numero, lista):

    lista_final = []

    for palabra in lista:

        if longitud(palabra) > numero:

            lista_final.append(palabra)

    return lista_final

lista = ['hola', 'palabra', 'ramon', 'estetoscopio', 'adios']

print(mas_larga(lista))

print(filtrar_palabras(5, lista))