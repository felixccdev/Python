# Tuplas (una vez creada no se puede variar, es inmutable)

#Existen dos formas de crear una tupla
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.88, "Felix", "Casero", "Felix")
my_other_tuple = (35, 60, 30)

print (my_tuple)
print(type(my_tuple))

print (my_tuple[0]) #Selecciono el elemento de la tupla posición 0
print(my_tuple[-1])
#print(my_tuple[4]) Si me paso del rango de la tupla da error
#print(my_tuple[6])

print(my_tuple.count("Felix")) #Cuenta las veces que aparece este valor en la tupla
print(my_tuple.index("Casero")) #Nos dice el índice o posición del valor buscado
print(my_tuple.index("Felix"))

#my_tuple[1] = 1.95 #La tupla no me deja cambiar valores, son inmutables le intento meter 1.95 en el valor 1 y no me deja
my_sum_tuple = my_tuple + my_other_tuple # Creamos una nueva tupla que es la suma de las 2 tuplas que tenemos
print(my_tuple + my_other_tuple)

print(my_sum_tuple[3:6]) #Me muestra los números de la tupla en ese rango entre el 3 y el 6 sin tener en cuenta el 6

my_tuple = list(my_tuple) #Transformo la tupla en una lista
print(type(my_tuple))

my_tuple[4] = "Manises SL" #Cambia texto "Felix" por "Manises SL" en el índice 4 de la lista
my_tuple.insert(1, "Azul") #Inserta texto en el índice 1 de la lista
my_tuple = tuple(my_tuple)#Vuelvo a convertir mi lista en tupla
print(my_tuple)
print(type(my_tuple))

# del my_tuple [2] #No permite eliminar un elemento de la tupla

del my_tuple #Borra la tupla por completo
# print(my_tuple) Me da error al imprimirla porque al deletearla no existe ya



