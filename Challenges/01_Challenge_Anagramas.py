# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

primera_palabra = input("Introduce la primera palabra ")
segunda_palabra = input("Introduce la segunda palabra ")

def es_anagrama(primera_palabra, segunda_palabra):
    # Convertir ambas palabras a minúsculas y quitar espacios en blanco
    primera_palabra = primera_palabra.lower().replace(" ", "")
    segunda_palabra = segunda_palabra.lower().replace(" ", "")

    # Si las palabras tienen diferente longitud, no pueden ser anagramas
    if len(primera_palabra) != len(segunda_palabra):
        return False

    # Crear diccionarios con las letras y su frecuencia en cada palabra
    dic1 = {}
    dic2 = {}

    for letra in primera_palabra:
        if letra in dic1:
            dic1[letra] += 1
        else:
            dic1[letra] = 1

    for letra in segunda_palabra:
        if letra in dic2:
            dic2[letra] += 1
        else:
            dic2[letra] = 1

    # Si los diccionarios son iguales, las palabras son anagramas
    if dic1 == dic2:
        return True
    else:
        return False

# Utilizamos la función para comprobar si son anagramas las palabras introducidas
if es_anagrama(primera_palabra, segunda_palabra):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")

