# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra en una frase que introduzca el usuario y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

def contar_palabras(frase):
    # Convertir la cadena de texto en minúsculas y dividirla en una lista de palabras
    palabras = frase.lower().split()

    # Crear un diccionario para almacenar la cantidad de veces que aparece cada palabra
    recuento = {}

    # Iterar a través de cada palabra en la lista de palabras
    for palabra in palabras:
        # Eliminar cualquier signo de puntuación alrededor de la palabra
        palabra = palabra.strip('.,!?¡¿-')

        # Si la palabra ya está en el diccionario, aumentar su valor en 1
        if palabra in recuento:
            recuento[palabra] += 1
        # De lo contrario, agregar la palabra al diccionario con un valor inicial de 1
        else:
            recuento[palabra] = 1

    # Devolver el diccionario con el recuento de palabras
    return recuento

# Pedir al usuario que introduzca una frase y almacenarla en una variable
frase_usuario = input("Introduce una frase: ")

# Llamar a la función contar_palabras con la frase del usuario como argumento
resultado = contar_palabras(frase_usuario)

# Imprimir el recuento de palabras
print("Recuento de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")
