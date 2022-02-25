#Definir una función superposicion() que tome dos listas y devuelva True si tienen 
#al menos 1 miembro en común o devuelva False de lo contrario. 

from pickle import FALSE

def superposicion(lista1, lista2):

    for i in lista1:

        for j in lista2:

            if i == j:

                return True

    return False

lista1 = [1, 2, 'hola', False, 3]
lista2 = [10, 3, 'adios, True']

print(superposicion(lista1, lista2))