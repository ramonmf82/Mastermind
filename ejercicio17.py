#Definir una lista con un conjunto de nombres, imprimir la cantidad que comienza con la letra a.
#También se puede hacer elegir al usuario la letra a buscar. 

def empieza_con(letra, lista):

    contador = 0

    for palabra in lista:

        if palabra.lower().startswith(letra.lower()):

            contador += 1

    return contador

lista = ['ramon', 'hola', 'lara', 'mariano', 'Raquel']
print(empieza_con('R', lista))