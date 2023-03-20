# Listas (se pueden modificar los elementos)

#Tenemos 2 formas para crear listas
my_list = list() 
my_other_list = []

print(len(my_list)) #Cuenta los elementos totales de la lista

my_list = [33, 22, 62 ,52, 30, 22, 45, 17]

print(my_list)
print(len(my_list))   #Muestra el número de elementos de la lista

my_other_list = [33, 1.88, "Felix", "Casero"] #Podemos guardar diferentes tipos de datos

print (type(my_list))
print (type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3]) # Si pongo un "-" Empieza a contar desde el último elemento de la lista
#print(my_other_list[4]) # Nos salimos del rango de la lista y da error
#print(my_other_list[-5]) # Nos salimos del rango de la lista y da error
print(my_list.count(22)) #Cuenta las veces que está el valor que le indicamos en el count, en este caso el nº 22

edad, altura, nombre, apellido = my_other_list #Damos nombres a las variables de la lista
print(nombre)

print(my_list + my_other_list) #Para unir 2 listas

my_other_list.append("Manises SL") #Inserta un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1,"Rojo") #Inserta en la posición que le digamos un nuevo elemento en la lista
print(my_other_list)

my_other_list[1] = "Naranja" #Sustituye el valor 1 de la lista por "Rojo"
print(my_other_list)

my_other_list.remove("Naranja") #Elimina elemento indicado de la lista
print(my_other_list)

my_list.remove(22) #Elimina 1er elemento que coincide en la lista si está repetido
print(my_list)

my_list.pop() #Elimina el último elemento de la lista pero lo guardo, el remove lo elimina
print(my_list)

print(my_list.pop(2)) #Elimina el elemento que le indico en este caso el de la posición 2
print(my_list)

my_pop_element = my_list.pop(2) #Guardo el elemento eliminado en la posición 2 en esta variable
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina el elemento de la lista del índice que le indiquemos en este caso el posición 2
print(my_list)

my_new_list = my_list.copy() #Copia la lista en este punto a una nueva variable

my_new_list.reverse() #Imprime la lista en el orden inverso
print(my_new_list)

my_new_list.sort() #Ordena los valores de menor a mayor y si fuera string por orden alfabético
print(my_new_list)

print(my_new_list[1:3]) #Imprime el elemento entre el 1 y el 2

my_list.clear() #Borra todos los elementos de la lista
print(my_list)
print(my_new_list)



