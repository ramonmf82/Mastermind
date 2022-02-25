#Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos

cadena = input("Introduzca un texto: ")

if cadena.isalpha():

    print("Son todo letras")

else:

    print("No son todo letras")