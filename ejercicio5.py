#Imprima los 100 primeros números de la sucesión de Fibonacci (sin recursión)

a1 = 1
a2 = 1

print(a1)
print(a2)

for i in range(99):

    a3 = a2 + a1
    a1 = a2
    a2 = a3

    print(a3)
