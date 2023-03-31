# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# - Expresión no balanceada: { a * ( c + d ) ] - 5 }

def balanced_expression(expression):
    # Creamos un diccionario con los delimitadores y sus contrapartes
    delimiters = {'(': ')', '{': '}', '[': ']'}
    # Creamos una lista para almacenar los delimitadores abiertos
    stack = []
    # Iteramos a través de cada carácter de la expresión
    for char in expression:
        # Si encontramos un delimitador de apertura, lo agregamos a la pila
        if char in delimiters.keys():
            stack.append(char)
        # Si encontramos un delimitador de cierre, comprobamos si es el correcto
        elif char in delimiters.values():
            # Si la lista está vacía, la expresión está desequilibrada
            if not stack:
                return False
            # Comprobamos si el delimitador de cierre coincide con el último delimitador de apertura
            if char != delimiters[stack.pop()]:
                return False
    # Si la lista está vacía al final, la expresión está equilibrada
    return not stack

# Ejemplos de uso
print(balanced_expression("{ [ a * ( c + d ) ] - 5 }")) # True
print(balanced_expression("{ a * ( c + d ) ] - 5 }")) # False
