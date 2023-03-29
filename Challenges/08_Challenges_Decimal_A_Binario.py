# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

# Pedimos al usuario que introduzca un número decimal
numero_decimal = int(input("Introduce un número decimal: "))

# Creamos una lista para almacenar los dígitos binarios del número
digitos_binarios = []

# Convertimos el número decimal a binario
while numero_decimal > 0:
    # Dividimos el número decimal entre 2 y obtenemos el resto
    resto = numero_decimal % 2
    # Agregamos el resto a la lista de dígitos binarios
    digitos_binarios.append(str(resto))
    # Dividimos el número decimal entre 2 y redondeamos hacia abajo
    numero_decimal //= 2

# Invertimos la lista de dígitos binarios para obtener el número binario correcto
digitos_binarios.reverse()

# Convertimos la lista de dígitos binarios en una cadena de texto y la imprimimos
numero_binario = ''.join(digitos_binarios)
print("El número binario es: " + numero_binario)
