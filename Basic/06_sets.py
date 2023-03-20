# Sets (No admite elementos repetidos)

# Tenemos 2 formas de crear un set
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente nos dice que es un diccionario

my_other_set = {"Felix", "Casero", 33}
print(type(my_other_set)) # Al meterle datos se convierte en set

print(len(my_other_set)) # Cuenta elementos que tiene el set

my_other_set.add("Manises SL")
print(my_other_set) # Un set no es una estructura ordenada, por lo tanto no podemos acceder a un elemento en una posición concreta

my_other_set.add("Manises SL")
print(my_other_set) # Un set no admite datos repetidos, si meto 2 datos repetidos uno no lo imprime

# Los sets nos permiten buscar dentro de ellos
print("Casero" in my_other_set) #Comprobamos si "Casero" existe en my_other_set y da True
print("Caseru" in my_other_set) #Comprobamos si "Caseru" existe en my_other_set y da False

my_other_set.remove("Casero") #Elimino este elemento del set
print(my_other_set)

my_other_set.clear() #Borra todos los elementos del set, pero no elimina el set
print(my_other_set)

del my_other_set #Elimina el set por completo, se carga la variable
#print(my_other_set)

my_set = {"Casero", "Felix", 33}
my_list = list (my_set) # Convierto el set en una lista
print(my_list)

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set) # Para unir 2 sets en un set
print(my_new_set.union({"Javascript", "C#"})) # Puedes añadir al set elementos directamente en el print

print(my_new_set.difference(my_set)) #De my_new_set le quitamos los elementos diferentes de my_set. Javascript y C# no aparecen porque no están almacenados en la variable solo hecho en el print
