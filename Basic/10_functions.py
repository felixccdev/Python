# Funciones (Centro en una función las operaciones para no repetir código)

# Cómo crear una función. "my_function" es el nombre que le he dado a la función

def my_function (): #Defino la función
    print("Esto es una función")

my_function () #Llamo a la función

def sum_two_values (first_value, second_value): #Función para sumar 2 valores
    print(first_value + second_value)

sum_two_values (5, 7) #Suma los números que le damos
sum_two_values (5232, 7235)
sum_two_values ("5", "7") #Concatena las 2 cadenas de texto
sum_two_values (1.4, 5.2) #Suma los números complejos 

def sum_two_values_with_return (first_value, second_value): 
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return (10, 5) #Le asignamos a una variable
print (my_result)

def print_name (name, surname):
    print(f"{name} {surname}") #La f es para que acceda a los valores de nombre y apellido y no me imprima {name} y {surname}

print_name(surname = "Casero", name = "Felix")

def print_name_with_default (name, surname, alias = "Sin alias"): #Si quiero un valor por defecto se lo añado como en el caso de "alias"
    print(f"{name} {surname} {alias}")

print_name_with_default ("Felix", "Casero") #Si no le paso el alias, me mete el alias por defecto
print_name_with_default ("Felix", "Casero", "Suco") #Si le paso el alias mete el alias que le paso

def print_texts (*text): #Al poner asterisco, le digo que puedo pasar los datos de text que quiera sin límite
    print(text)

print_texts ("Hola", "Python", "Suco")

def print_upper_texts (*texts): #Función para pasar los textos que le paso a la función a mayúsculas
    for text in texts:
        print(text.upper())

print_upper_texts ("Hola", "Python", "Suco")