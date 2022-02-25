#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que 
#evaluar la cadena y decir cuantas letras mayúsculas tiene.

palabra = input("Introduce un palabra: ")

contador = 0

for letra in palabra:

    if letra.isupper():

        contador += 1

print(f"El texto: {palabra} contiene {contador} mayúsculas")
