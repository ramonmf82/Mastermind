#Definir un histograma procedimiento() que tome una lista de números enteros e 
#imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

def procedimiento(lista):

    resultado = ''

    for contador in lista:

        for i in range(contador):

            resultado += '*'

            if i == contador - 1:

                resultado += '\n'

    return resultado

print(procedimiento([1, 4, 3, 7, 10, 8]))