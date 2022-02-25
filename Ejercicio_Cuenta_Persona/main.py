from Cuenta import *
from Persona import *
from Cuenta_joven import *

p = Persona("ramon", 23, 12345678)

print(p.es_mayor_de_edad())

print(p.get_dni())

c = Cuenta_joven(p, 1000, 10)

c.ingresar(200)

c.mostrar()