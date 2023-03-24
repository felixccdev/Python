# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

#Este programa define una función llamada invertir_cadena que toma como parámetro una cadena y devuelve una cadena con los caracteres invertidos en orden. 
#El algoritmo es muy sencillo: convierte la cadena a una lista de caracteres, intercambia los caracteres en los extremos de la lista usando un bucle while, 
#y luego convierte la lista de caracteres de vuelta a una cadena.

def invertir_cadena(cadena):
    # Convertir la cadena a una lista de caracteres
    lista_caracteres = list(cadena)
    
    # Obtener el índice del primer y último caracter
    indice_primero = 0
    indice_ultimo = len(lista_caracteres) - 1
    
    # Intercambiar los caracteres en los extremos de la lista
    while indice_primero < indice_ultimo:
        # Guardar el primer caracter
        temp = lista_caracteres[indice_primero]
        
        # Reemplazar el primer caracter con el último
        lista_caracteres[indice_primero] = lista_caracteres[indice_ultimo]
        
        # Reemplazar el último caracter con el primer
        lista_caracteres[indice_ultimo] = temp
        
        # Avanzar al siguiente y anterior caracteres
        indice_primero += 1
        indice_ultimo -= 1
    
    # Convertir la lista de caracteres a una cadena
    cadena_invertida = "".join(lista_caracteres)
    
    # Retornar la cadena invertida
    return cadena_invertida

cadena = input("Introduce la cadea de texto que quieras invertir: ")
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida) 

