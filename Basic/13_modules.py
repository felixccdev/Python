# Módulos (es la librería para llamar a otros ficheros Python y así poder escalar y dar seguridad a mi programa)

import my_module #Importa este archivo

my_module.sumValues(5, 3, 1)
my_module.printValue("Hola Python!")

from my_module import sumValues, printValue #Importa estas 2 funciones del archivo my_module

sumValues(5, 3, 1)
printValue("Hola python")

# También se pueden importar módulos del sistema

import math #Este módulo incluye funciones de operaciones matemáticas

math.pi #Accedemos al valor del número PI

print(math.pi) # Imprime el número PI
print(math.pow(2, 8)) # Nos da la potencia de 2 elevado a 8
print(math.isqrt(9)) # Nos da la raíz cuadrada de 9

from math import pi as PI_VALUE #Importamos Pi y lo asignamos a la varibale que hemos creado PI_VALUE
print(PI_VALUE)


