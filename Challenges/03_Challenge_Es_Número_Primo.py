# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

numero = int(input("Introduce un número para comprobar si es primo "))

# Función para calcular si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Utilizamos la función anterior con el número que hemos introducido por terminal
if es_primo(numero):
    print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")

# Imprime listado con los 100 primeros número primos
print("Números primos entre 1 y 100:")
for numero in range(1, 101):
    if es_primo(numero):
        print(numero)