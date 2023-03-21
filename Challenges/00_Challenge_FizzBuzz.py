#Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#Le añado la mejora de que los números del rango los añade el usuario a su gusto

numero_1 = int(input ("Introduce el primer número del rango "))
numero_2 = int(input ("Introduce el segundo número del rango "))

my_list = range (numero_1, numero_2)

for number in my_list:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0: 
        print("buzz")
    else:
        print(number)