# Condicionales

my_condition = False

if my_condition: #Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_condition = 5 * 5

if my_condition == 11: # Comprueba si la variable es igual a 11  
    print("Se ejecuta la condición del segundo if")

print("La ejecución continúa")

if my_condition == 10: # Comprueba si la variable es igual a 10  
    print("Se ejecuta la condición del segundo if")

print("La ejecución continúa")

if my_condition > 10: # Comprueba si la variable es mayor que 10  
    print("Es mayor que 10")
else: #Se imprime si no se cumple la condición
    print("Es menor o igual que 10")

print("La ejecución continúa")

if my_condition > 10 and my_condition < 20: #El if tiene que cumplir las 2 condiciones
    print("Es mayor que 10 y menor que 20")
else: 
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")

if my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: #If y elif necesitan siempre una condición. Elif está dentro de un If
    print("Es igual a 25")
else: 
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

my_string = "Mi cadena de texto"

if my_string: #Si le metemos una cadena de texto vacía la variable tendría valor False
    print("Mi cadena de texto no está vacía")

if my_string == "Mi cadena de textoooo":
    print("Estas cadenas de texto coinciden")

my_string = "" #Damos valor de Cadena de texto vacía

if not my_string: #Negamos que mi cadena de texto es vacía
    print("Mi cadena de texto está vacía")
