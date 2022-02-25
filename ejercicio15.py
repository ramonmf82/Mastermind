#Construir un pequeño programa que convierta números binarios en enteros.

binario = int(input("Introduce un número binario: "))

contador = 0
resultado = 0

while binario > 0:

    parcial = binario % 10

    binario = binario // 10

    if parcial == 1:

        resultado += 2 ** contador

    contador += 1

print(resultado)
