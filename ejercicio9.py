#Definir una función inversa() que calcule la inversión de una cadena. 
#Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):

    total = ''

    for i in cadena:

        total = i + total

    return total

#Definir una función es_palindromo() que reconoce palíndromos

def es_palindromo(cadena):

    reversa = inversa(cadena)

    return reversa == cadena

cadena = input("Introduce un texto: ")
print(inversa(cadena))
print(es_palindromo(cadena))