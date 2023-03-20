def calcular_letra_dni(numero_dni):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    letra = letras[numero_dni % 23]
    return letra

numero_dni = int(input('Introduce el número de DNI (sin letra): '))
letra_dni = calcular_letra_dni(numero_dni)
print(f'La letra correspondiente al número de DNI {numero_dni} es {letra_dni}.')
