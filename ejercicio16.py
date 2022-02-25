#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

anno_actual = int(input("Introduce el año en curso: "))

anno = [0,0,0]
cumple = [0,0,0]

for i in range(3):

    anno[i] = int(input("Introduce el año de nacimiento: "))
    cumple[i] = anno_actual - anno[i]

for i in range(3):

    print(f"El sujeto {i + 1} va a cumplir {cumple[i]} años.")