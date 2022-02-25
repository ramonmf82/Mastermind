#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números 
#de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(array):

    total = 0

    for i in array:

        total += i

    return total

def multip(array):

    total = 1

    for i in array:

        total *= i

    return total

vector = [1,2,3,4,5]
print(sum(vector))
print(multip(vector))