import pandas as pd
import numpy as np
import matplotlib as mp

##PUNTO 1
#-------------------------------------------------------------------------------------
# Se crean los vectores a y b 
vector_a = np.array([3.1, 1, -0.5, -3.2, 6]) 
vector_b = np.array([1, 3, 2.2, 5.1, 1])

#-------------------------------------------------------------------------------------
# Producto escalar de los vectores a y b
# para realizar el producto escalar se requiere que ambos vectores sean de la misma longitud 
# Tambien se requiere que los vectores sean tipo array.
product_sc = vector_a @ vector_b 
print (product_sc)

#-------------------------------------------------------------------------------------
# Multiplicacion punto a punto de ambos vectores
product_mtr = vector_a * vector_b 
print (product_mtr)

#-------------------------------------------------------------------------------------
Matriz = np.array([[2, -1, -3], [4, 1.5, -2.5], [7.3, -0.9, 0.2]]) #Matriz A
Matriz = np.transpose(Matriz) # Transpuesta de la matriz A
print(Matriz)

#-------------------------------------------------------------------------------------
# la funcion ones crea una matriz de unos de las dimensiones que se le otorguen
Matriz_ones = np.ones((5,3))
# El primer argumento recibe una tupla con las dimensiones de la matriz, los otros dos argumentos 
# reciben el tipo de dato que se ingresa y el orden.
print(Matriz_ones)