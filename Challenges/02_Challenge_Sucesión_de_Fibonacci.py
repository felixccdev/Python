# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

# Establecemos los dos primeros números de la serie
num_1 = 0
num_2 = 1

# Imprimimos los dos primeros números
print(num_1)
print(num_2)

# Iteramos para obtener los siguientes 48 números
for number in range(48):
    # Calculamos el siguiente número de la serie como la suma de los dos anteriores
    num_3 = num_1 + num_2
    # Imprimimos el siguiente número
    print(num_3)
    # Actualizamos los valores de los números anteriores para calcular el siguiente número
    num_1 = num_2
    num_2 = num_3
