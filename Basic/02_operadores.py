# Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)      #Nos calcula el resto de esa división
print(10 // 3)    # Es una división que nos da un resultado entero
print(2 ** 3)       #Sirve para hacer un exponente

# Operadores Aritméticos

print ("Hola " + "Python " + "¿Qué tal?")
print ("Hola " + str (5))

print(2**3 + 3 - 7 / 1 //4)
print ("Hola " * (2**3))

my_int = 2.5 * 2
print ("Hola " * int(my_int))

# Operadores Comparativos

#Comparamos números

print (3 > 4)
print (3 < 4)
print (3 <= 4)
print (3 >= 4)
print (3 != 4) 
print (3 + 4 == 7) 

# Comparamos cadenas de texto. Comprueba el orden alfabético no el número de caracteres

print ("Hola" > "Python")
print ("Hola" < "Python")
print ("Hola" <= "Python")
print (len("Holarr") >= len("Zolar")) #Para comparar por número de caracteres habría que hacerlo con "len"
print ("Hola" == "Python") 
print ("Hola" != "Python") 

# Operadores Lógicos

print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or "Hola" > "Python")
print (3 > 4 or ("Hola" > "Python" and 4 == 4)) 
print (not (3 > 4))
