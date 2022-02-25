#Escriba un programa en Python que realice las siguientes 9 multiplicaciones.
#1 · 1
#11 · 11
#111 · 111
#.
#.
#.
#111111111 · 111111111

numero = 0

for i in range(9):

    numero += 10**i
    res = numero * numero
    print(f"{numero} x {numero} = {res}")

    