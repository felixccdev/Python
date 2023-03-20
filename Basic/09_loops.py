# Bucles (Hay varios tipos)

# Bucle While (Sirve para que un código se repita varias veces en función de una condición)

my_condition = 0

while my_condition < 10:  #Se ejecuta hasta que my_condition vale 10
    print(my_condition)
    my_condition += 1 #Al valor que tenga en este punto la condición se le añade 1
else: # Es opcional de poner el else. Cuando deja de cumplirse el while se ejecuta el else
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa") # Se ejecuta cuando el bluce while termina

while my_condition < 20:
    my_condition += 1 
    if my_condition == 15:
            print("Se detiene la ejecución")
            break # Cuando llega al valor 15 se detiene la ejecución
    print (my_condition)       
    
print("La ejecución continúa")

# Bucle For (Se va a ejecutar tantas veces como elementos tenga el listado que le damos)

my_list = [35, 24, 62 ,52, 30, 30, 17]

for element in my_list: #Imprime los elementos de la lista
    print (element)

my_tuple = (33, 1.88, "Felix", "Casero", "Felix")

for element in my_tuple: #Imprime los elementos de la tupla
    print (element)

my_set = {"Casero", "Felix", 33}

for element in my_set: #Imprime los elementos del set
    print (element)

my_dict = {"Nombre": "Felix", "Apellido": "Casero", "Edad":33, 1: "Python"}

for element in my_dict: #Imprime las keys del diccionario
    print (element)

for element in list(my_dict.values()): #Imprime los valores de las keys del diccionario
    print (element)

for element in my_dict: 
    print (element)
    if element == "Edad": #Cuando llega a la key Edad se para el bucle
        break # Detiene el bucle
else:
    print("El bucle para for ha finalizado")

for element in my_dict: 
    print (element)
    if element == "Edad": #Cuando llega a la key Edad se para el bucle
        continue # Vuelve al inicio del for y no ejecuta la línea que está debajo de continue
    print("Se ejecuta")
else:
    print("El bucle para for ha finalizado")
