#Definir una función generar_n_caracteres() que tome un entero n y devuelva el 
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar(numero, caracter):

    resultado = ''

    for i in range(numero):

        resultado += caracter

    return resultado

print(generar(23, 'X'))