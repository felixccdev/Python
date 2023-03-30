
#Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

# Metemos el código morse en un diccionario
MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.'}

# Convierte un texto a su equivalente en código Morse
def encode_morse(text):
    morse_code = ''  # Se crea una variable vacía para guardar el código Morse resultante
    for letter in text.upper():  # Se itera sobre cada letra del texto en mayúsculas
        if letter == ' ':  # Si la letra es un espacio, se agrega un espacio al código Morse
            morse_code += ' '
        else:  # Si no es un espacio, se busca la letra en el diccionario MORSE_CODE y se agrega su equivalente en código Morse al código Morse resultante
            morse_code += MORSE_CODE.get(letter, '') + ' '
    return morse_code  # Se devuelve el código Morse resultante

# Convierte un código Morse a su equivalente en texto
def decode_morse(morse_code):
    text = ''  # Se crea una variable vacía para guardar el texto resultante
    for code in morse_code.split(' '):  # Se separa el código Morse en sus símbolos individuales utilizando el espacio como separador
        if code == '':  # Si el símbolo es un espacio, se agrega un espacio al texto resultante
            text += ' '
        else:  # Si no es un espacio, se busca el símbolo en el diccionario MORSE_CODE y se agrega su clave (es decir, la letra o número) al texto resultante
            text += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(code)]
    return text  # Se devuelve el texto resultante

# Función principal del programa
def main():
    text = input('Introduzca el texto o código Morse: ')  # Se pide al usuario que introduzca un texto o código Morse
    if all(x in '.- ' for x in text):  # Se determina si la entrada es código Morse o texto
        result = decode_morse(text)  # Si es código Morse, se decodifica utilizando la función decode_morse
    else:
        result = encode_morse(text)  # Si es texto, se codifica utilizando la función encode_morse
    print(result)  # Se imprime el resultado

# Se llama a la función main si el programa es ejecutado directamente (es decir, no es importado como módulo)
if __name__ == '__main__':
    main()  
