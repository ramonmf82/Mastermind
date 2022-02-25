from array import array


def decimal_a_romano(decimal):

    resultado = ''

    millar = decimal // 1000

    if millar == 1:

        resultado += 'M'

    elif millar == 2:

        resultado += 'MM'

    elif millar == 3:

        resultado += 'MMM'

    elif millar == 4:

        resultado += 'MMMM'

    decimal = decimal % 1000
    centena = decimal // 100

    if centena == 1:

        resultado += 'C'

    elif centena == 2:

        resultado += 'CC'

    elif centena == 3:

        resultado += 'CCC'

    elif centena == 4:

        resultado += 'CD'

    elif centena == 5:

        resultado += 'D'

    elif centena == 6:

        resultado += 'DC'

    elif centena == 7:

        resultado += 'DCC'

    elif centena == 8:

        resultado += 'DCCC'

    elif centena == 9:

        resultado += 'CM'

    decimal = decimal % 100
    decena = decimal // 10

    if decena == 1:

        resultado += 'X'

    elif decena == 2:

        resultado += 'XX'

    elif decena == 3:

        resultado += 'XXX'

    elif decena == 4:

        resultado += 'XL'

    elif decena == 5:

        resultado += 'L'

    elif decena == 6:

        resultado += 'LX'

    elif decena == 7:

        resultado += 'LXX'

    elif decena == 8:

        resultado += 'LXXX'

    elif decena == 9:

        resultado += 'XC'

    unidad = decimal % 10

    if unidad == 1:

        resultado += 'I'

    elif unidad == 2:

        resultado += 'II'

    elif unidad == 3:

        resultado += 'III'

    elif unidad == 4:

        resultado += 'IV'

    elif unidad == 5:

        resultado += 'V'

    elif unidad == 6:

        resultado += 'VI'

    elif unidad == 7:

        resultado += 'VII'

    elif unidad == 8:

        resultado += 'VIII'

    elif unidad == 9:

        resultado += 'IX'
    
    return resultado

def romano_a_decimal(romano):

    array = list(romano)
    array.append('a')

    i = 0
    resultado = 0

    while i < len(array):

        if array[i] == 'M':

            resultado += 1000

        if array[i] == 'D':

            resultado += 500
        
        if array[i] == 'L':

            resultado += 50

        if array[i] == 'V':

            resultado += 5

        if array[i] == 'C' and array[i + 1] == 'M':

            resultado += 900

            i += 1

        elif array[i] == 'C' and array[i + 1] == 'D':

            resultado += 400

            i += 1

        elif array[i] == 'C' and array[i + 1] != 'M' and array[i + 1] != 'D': 

            resultado += 100

        if array[i] == 'X' and array[i + 1] == 'C':

            resultado += 90

            i += 1

        elif array[i] == 'X' and array[i + 1] == 'L':

            resultado += 40

            i += 1

        elif array[i] == 'X' and array[i + 1] != 'C' and array[i + 1] != 'L': 

            resultado += 10

        if array[i] == 'I' and array[i + 1] == 'X':

            resultado += 9

            i += 1

        elif array[i] == 'I' and array[i + 1] == 'V':

            resultado += 4

            i += 1

        elif array[i] == 'I' and array[i + 1] != 'X' and array[i + 1] != 'V': 

            resultado += 1
    
        i += 1

    return resultado

num_dec = int(input("Escriba un número: "))

print(f"El número {num_dec} en romanos es: {decimal_a_romano(num_dec)}")

num_rom = input("Escriba el número en romano: ")

print(f"El número {num_rom} en decimal es: {romano_a_decimal(num_rom)}")
