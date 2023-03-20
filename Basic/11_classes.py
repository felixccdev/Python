# Clases (Sirven para definir entidades, en este caso una persona)

# Para definir una clase
class MyEmptyPerson: #El nombre de la clase se pone en mayúscula la primera letra de cada palabra
    pass #Evita que de error si la clase está vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person: #Vamos a dar parámetros a este objeto persona (nombre y apellido)
    def __init__(self, name, surname, alias = "Sin alias"): #init sirve para crear un constructor de clase
        self.name = name #El uso del self es obligatorio, crea las propiedades dentro de la clase persona
        self.surname = surname
        self.alias= alias

    def walk(self): # Creo una función de que la persona camina
        print(f"{self.name} {self.surname} ({self.alias}) está caminando")

my_person = Person("Felix","Casero") #Aquí person ya puede recibir los valores nombre y apellido
print(my_person.name) #Imprime el nombre
print(f"{my_person.name} {my_person.surname} {my_person.alias}") #Imprime nombre y apellido
my_person.walk() #Imprime la función walk con el nombre y el apellido que le hemos metido formateado

my_other_person = Person ("Felix", "Casero", "Manis") #Nueva variable
print(f"{my_other_person.name} {my_other_person.surname} {my_other_person.alias}") 
my_other_person.walk()
my_other_person.name = "Héctor de León (El loco de los perros)" #Cambio el valor del nombre de Felix a Hector el Loco de los Perros
print(my_other_person.name, my_other_person.surname, my_other_person.alias)