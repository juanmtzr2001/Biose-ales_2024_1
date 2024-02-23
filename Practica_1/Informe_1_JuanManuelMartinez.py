import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


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
Matriz_T = np.transpose(Matriz) # Transpuesta de la matriz A
print(Matriz_T)

#-------------------------------------------------------------------------------------
# la funcion ones crea una matriz de unos de las dimensiones que se le otorguen
Matriz_ones = np.ones((5,3))
# El primer argumento recibe una tupla con las dimensiones de la matriz, los otros dos argumentos 
# reciben el tipo de dato que se ingresa y el orden.
print(Matriz_ones)


# La funcion round sirve para redondear hacia abajo los valores de una matriz, un vector o un numero cualquiera 
# al numero de decimales que se desee. 
#El primer argumento es el dato que se quiere redondear, el segundo el numero de decimales al que se quiere
#Redondear y el tercero es si se quiere especificar algun array donde guardar el resultado

Matriz_B = np.array([[2, -1.542, -3.487], [4, 1.587, -2.597], [7.321, -0.943, 0.274]]) # Se creo otra matriz con mas decimales
Matriz_round = np.round(Matriz, decimals = 1, out = None)
print(Matriz_round)

# La funcion ceil sirve para redondear a valores enteros hacia arriba, datos de una matriz, un vector o un numero cualquiera 
# al numero de decimales que se desee. 
#El primer argumento es el dato que se quiere redondear, el segundo el numero de decimales al que se quiere
#Redondear y el tercero es si se quiere especificar algun array donde guardar el resultado

Matriz_ceil = np.ceil(Matriz_B)
print(Matriz_ceil)

# La funcion ceil sirve para redondear a valores enteros hacia abajo, datos de una matriz, un vector o un numero cualquiera 
# al numero de decimales que se desee. 
#El primer argumento es el dato que se quiere redondear, el segundo el numero de decimales al que se quiere
#Redondear y el tercero es si se quiere especificar algun array donde guardar el resultado

Matriz_floor = np.floor(Matriz_B)
print(Matriz_floor)

#-----------------------------------------------------------------------------------------------------
# Para al valor de una fila y columna especifica del arreglo se escribe Matriz[pos_1, pos_2], donde pos_1 corresponde al numero
# de fila y pos_2 al numero de columna, teniendoe n cuenta que en python se empieza a contar desde cero.

print('__________________________________________________________')
print(Matriz)
print('__________________________________________________________')
num_fila = 1 # Se pide ubicar la fila 1
num_col = 3 # y la columna 3
print(Matriz[num_fila-1, num_col-1]) # Ya que empieza desde a contar desde cero

#--------------------------------------------------------------------------------------------------------
# Se quiere obtener la segunda fila completa, para ello se escribe la fila especifica que se requeire y en el sgte argumento
# Se especifica que se requieren todos los datos de las columnas que conforman esa fila, de esta forma

num_fila = 2
print(Matriz[num_fila-1, :]) # Los : solos quiere decir que se requieren todos los datos que conforman la fila
#-----------------------------------------------------------------------------------------------------

#Para saber las dimensiones de una matriz se utiliza el comando .shape que entrega una tupla con las dimensiones de la matriz

print(Matriz.shape)

#-----------------------------------------------------------------------------------------------------
# Para construir las dos senales, primero se crea un vector de tiempo llamado tiempo_n
tiempo_n = np.linspace(0, 100, 202)
# a partir del vector de tiempo se construye la ecuacion

y = np.sin(np.pi*0.12*(tiempo_n)) 

# De igual manera se construye la sigueinte senoidal

y2 = np.cos(2*(np.pi)*0.03*(tiempo_n))

# Se crean la tercera y cuarta senal con las operaciones de suma y multiplicacion

senal_sum = y + y2
senal_t = y*y2

plt.figure()
plt.plot(tiempo_n,y, label = 'Y')
plt.plot(tiempo_n,y2, label = 'Y2')

plt.show()
