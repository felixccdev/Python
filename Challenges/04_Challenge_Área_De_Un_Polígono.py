 # Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 # La función recibirá por parámetro sólo UN polígono a la vez.
 # Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # Imprime el cálculo del área de un polígono de cada tipo.

tipo = input("Introduce el tipo de polígono ")
base = int(input("Introduce la base "))
altura = int(input("Introduce la altura "))

#Función para calcular el área en función del tipo de polígono, la base y la altura
def calcular_area_poligono(tipo, base, altura):
    if tipo == "Triángulo":
        area = 0.5 * base * altura
        print(f"El área del Triángulo es: {area}")
        return area
    elif tipo == "Cuadrado":
        area = base * altura
        print(f"El área del Cuadrado es: {area}")
        return area
    elif tipo == "Rectángulo":
        area = base * altura
        print(f"El área del Rectangulo es: {area}")
        return area
    else:
        print("Tipo de polígono no soportado, introduce: Triángulo, Cuadrado ó Rectángulo")

# Imprimir el área del polígono llamando a la función con los inputs dados al principio
calcular_area_poligono(tipo, base, altura)


