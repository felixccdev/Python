# Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
# Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

import requests

def calculate_aspect_ratio(url):
    response = requests.get(url, stream=True)
    response.raw.decode_content = True
    width = height = 0
    for chunk in response.iter_content(chunk_size=1024):
        if b'\x89PNG\r\n\x1a\n' in chunk:
            # Obtener la anchura y la altura de la cabecera PNG
            width, height = chunk[16:20], chunk[20:24]
            width = int.from_bytes(width, byteorder='big')
            height = int.from_bytes(height, byteorder='big')
            break
        elif b'\xff\xd8' in chunk:
            # Obtener la anchura y la altura de la cabecera JPEG
            data = chunk.split(b'\xff\xc0', 1)[1]
            width = int.from_bytes(data[3:5], byteorder='big')
            height = int.from_bytes(data[5:7], byteorder='big')
            break
    if width > 0 and height > 0:
        gcd = find_gcd(height, width)
        aspect_ratio = f"{height // gcd}:{width // gcd}"
        return aspect_ratio
    else:
        return "Error: no se pudo calcular el aspect ratio"

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

url = input("Introduce la URL de la imagen: ")
aspect_ratio = calculate_aspect_ratio(url)
print(f"El aspect ratio de la imagen es: {aspect_ratio}")





