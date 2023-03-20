# Diccionarios

# Dos formas de crear un diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Tenemos una clave y le asignamos un valor, sirve para relacionar datos
my_other_dict = {"Nombre": "Felix", "Apellido": "Casero", "Edad":33, 1: "Python"}

my_dict = {
    "Nombre": "Felix", 
    "Apellido": "Casero", 
    "Edad":33, 
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Le metemos un set dentro del diccionario
    1:1.89 # Mi estatura
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # Cuenta elementos del diccionario. Tiene 4
print(len(my_dict)) # Tiene 5 elementos, el set cuenta solo como un elemento

print(my_dict["Nombre"]) # Me imprime el valor de esta clave del diccionario

my_dict["Nombre"] = "Pedro" #Cambio el valor de la clave "Nombre" de Felix a Pedro
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Sayago" # Añadimos un campo a nuestro diccionario
print(my_dict)

del my_dict ["Calle"] #Elimina un elemento concreto de nuestro diccionario
print(my_dict)

print("Casero" in my_dict) # Busca por el nombre del campo, por eso da Falso
print("Apellido" in my_dict) # Da True porque ha buscado el campo
print(my_dict["Apellido"]) #Nos muestra el elemento del campo Apellido

print(my_dict.items()) # Nos da un listado con todos los items
print(my_dict.keys()) # Nos da un listado de los campos en formato lista
print(my_dict.values()) # Nos da los valores de los campos
print(my_dict.fromkeys(("Nombre",1, "Piso"))) # Nos crea un nuevo diccionario

my_list = ["Nombre",1, "Piso"]

my_new_dict = dict.fromkeys(my_list) # Creamos un diccionario a partir de una lista
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre",1,"Piso")) # Hace lo mismo que el anterior
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict)) # Me copia las claves del diccionario my_dict pero sin los datos de cada clave
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Felix", "Casero")) #Le metemos Felix y Casero a todos los elementos del diccionario
print(my_new_dict)

print(list(my_new_dict)) # Transformo el diccionario en una lista
print(tuple(my_new_dict)) # Transformo el diccionario en una tupla
print(set(my_new_dict)) # Transformo el diccionario en un set