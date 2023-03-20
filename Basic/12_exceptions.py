# Manejo de Errores

numberOne = 5 
numberTwo = 1

numberTwo = "1"

if type(numberTwo) == int: #Con esto solo se ejecuta si numberTwo es un entero
    print(numberOne + numberTwo)
else:  
    print("No se cumplió")

#Para evitar este tipo de errores (que no tenemos porque conocer) hacemos esto:

# 1. Tenemos el modelo try - except
try:
    print(numberOne + numberTwo) #Si da fallo dentro del try, el programa no se detiene, pero salta a ejecutar la parte de except
    print("No se ha producido un error")
except:  
    print("Se ha producido un error") #Se ejecuta si se produce una excepción

# 2. Tenemos el otro modelo try - except - else
try:
    print(numberOne + numberTwo) #Si da fallo dentro del try, el programa no se detiene, pero salta a ejecutar la parte de except
    print("No se ha producido un error")
except:  
    print("Se ha producido un error")
else: #Es opcional poner el else
    print("La ejecución continúa correctamente") #Este else si no se produce una excepción no se ejecuta
finally: #Es opcional poner el finally
    print("La ejecución continúa") #El finally se ejecuta siempre falle o no la aplicación

#Captura de Excepciones por Tipo

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except ValueError: #Captura solo errores ValueError
     print("Se ha producido un ValueError")
except TypeError:  #Solo captura errores del tipo TypeError, si sale otro error diferente vuelve a petar el programa
    #Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")

#Captura de la información de la excepción

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error")
except ValueError as error: #De este modo registramos el error
     print(error)
except Exception as error: #Con Exception sea cual sea el error nos lo controla y captura
     print(error)