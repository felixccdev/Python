import numpy as np

#Crear un vector con valores dentro del rango 10 a 49
vector = np.arange(10,50)
print(vector)

#Invertir el vector

vector_invertido = vector[::-1]
print (vector_invertido)

#Crear una matriz 3x3 con valores de 0 a 8

matriz = np.arange(0,9).reshape(3,3)
print (matriz)

#Encontrar los indices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]

a = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
indices_distintos_de_cero = np.argwhere( a!=0 )
print(indices_distintos_de_cero)

#Crear una matriz identidad de 6x6

matriz_6x6 = np.identity(6)
print (matriz_6x6)

#Crear una matriz con valores al azar con forma 3x3x3
matriz_random = np.random.random((3,3,3))
print(matriz_random)

#Encontrar los indices de los valores minimos y maximos de la anterior matriz
print( matriz_random.argmax() )
print( matriz_random.ravel()[matriz_random.argmax()] )

print(matriz_random)
print(np.unravel_index(matriz_random.argmax(), matriz_random.shape))
matriz_random[np.unravel_index(matriz_random.argmax(), matriz_random.shape)]

#Crear una matriz de 10x10 con 1's en los bordes y 0 en el interior (con rangos de indices)

matriz_10x10 = np.ones((10,10))

matriz_10x10[1:-1,1:-1] = 0
print (matriz_10x10)

#Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4

matriz_5x5 = np.tile( np.arange(0,5) , 5).reshape(5,5)
print(matriz_5x5)

