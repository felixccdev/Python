# Strings

my_string = "My String" #Comillas dobles o simples funcionan igual
my_other_string = 'My String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

# String con salto de línea

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

# String con tabulación

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

# String con escapado

my_scape_string = "\tEste es un string \n \tescapado"
print(my_scape_string)

# Formateo (para poner llaves se pulser Control+Atl+Tecla Llave)

name, surname, age = "Felix", "Casero", 33

print("Mi nombre es {} {} y mi edad es {}" .format(name,surname,age)) # Con la función .format se usan llaves
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age)) # Con el % también sirve. %s devuelve texto, %d devuelve enteros
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta es la mejor forma de hacerlo

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(d)

# División (coge los caracteres del 1 al 3 son contar el primero)

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:] #Coge de la letra 1 hasta el final
print(language_slice)

language_slice = language [-2] #Coge la 2a desde el final
print(language_slice)

language_slice = language [0:6:2] #Coge del rango y coge las letras de 2 en 2
print(language_slice)

# Reverse

reversed_language = language [::-1]
print(reversed_language)

#Funciones del sistema

print(language.capitalize()) #Primera letra en mayúscula
print(language.upper()) # Todas las letras en mayúscula
print(language.count("t")) # Todas las "t" que contiene la variable
print(language.isnumeric()) #Comprueba si es un número
print("1".isnumeric()) #Meto un número y comprueba si es número
print(language.lower()) #Todas en minúscula
print(language.upper().isupper()) #La pasa a mayúscula y comprueba si es mayúscula
print(language.startswith("py")) #Comprueba si la variable empieza por "py"
print("py" == "Py") #Comprueba que "py" es igual que "Py" y es False porque diferencia mayúsculas