#Variables

my_string_variable = "My String variable"
print (my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str (my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print (my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable,my_int_to_str_variable,my_int_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)

#Algunas Funciones del sistema

print(len(my_string_variable)) #La funcion "len" cuenta los caracteres de una variable

#Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Felix", "Casero", "FelixCC", 33
print("Me llamo:", name, surname,". Mi edad es:", age, "Y mi alias es:", alias)

#Función para entrada de datos
name = input ("¿Cómo te llamas: ")
age = input ("¿Cuántos años tienes? ")

print ("Me llamo:", name)
print("Tengo", age, "años")

#Cambiamos el tipo de la variable
name = 33
age = "Felix"

print ("Me llamo:", name)
print("Tengo", age, "años")

#¿Forzamos el tipo de la variable?
address: str = "Mi dirección"
address = 32

print (type (address))

