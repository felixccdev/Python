# Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
# Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

import requests

# Función que calcula el aspect ratio a partir de una URL de imagen
def calculate_aspect_ratio(url):
    # Realizar petición GET a la URL de la imagen
    response = requests.get(url, stream=True)
    # Decodificar contenido de la respuesta
    response.raw.decode_content = True
    width = height = 0
    # Leer la imagen por chunks de 1024 bytes
    for chunk in response.iter_content(chunk_size=1024):
        # Si se encuentra la cabecera PNG
        if b'\x89PNG\r\n\x1a\n' in chunk:
            # Obtener la anchura y la altura de la cabecera PNG
            width, height = chunk[16:20], chunk[20:24]
            width = int.from_bytes(width, byteorder='big')
            height = int.from_bytes(height, byteorder='big')
            break
        # Si se encuentra la cabecera JPEG
        elif b'\xff\xd8' in chunk:
            # Obtener la anchura y la altura de la cabecera JPEG
            data = chunk.split(b'\xff\xc0', 1)[1]
            width = int.from_bytes(data[3:5], byteorder='big')
            height = int.from_bytes(data[5:7], byteorder='big')
            break
    # Si se encontró la anchura y la altura de la imagen
    if width > 0 and height > 0:
        # Calcular el gcd de la anchura y la altura para obtener el aspect ratio
        gcd = find_gcd(height, width)
        aspect_ratio = f"{height // gcd}:{width // gcd}"
        return aspect_ratio
    else:
        return "Error: no se pudo calcular el aspect ratio"

# Función que calcula el gcd de dos números
def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

# Pedir al usuario la URL de la imagen
url = input("Introduce la URL de la imagen: ")
# Calcular el aspect ratio a partir de la URL de la imagen
aspect_ratio = calculate_aspect_ratio(url)
# Imprimir el aspect ratio
print(f"El aspect ratio de la imagen es: {aspect_ratio}")






