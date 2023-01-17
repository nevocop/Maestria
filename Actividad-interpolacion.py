# INTERPOLACION MECANISMO EN LINEA RECTA DE HOEKEN____
# Se importan las librerias necesarias para el algoritmo
# La clase scipy.interpolate se utiliza para interpolar una función unidimensional
from scipy.interpolate import interp1d
# Se importa la librería Matplotlib con un alias, para graficas
import matplotlib.pyplot as plt
# Se importa la librería Numpy con un alias, para hacer los cálculos
import numpy as np
#import sympy as sym

# Se ingresan los datos del mecanismo de linea recta de Hoeken
X = [20, 40, 60, 80, 100, 120, 140, 160, 180]
Y = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181]
 
# Punto en el que se quiere interpolar
interpolar_x = 55
 
# Resolviendo y buscando la interpolación
y_interp = interp1d(X, Y)
print("El valor de Y en X = {} es".format(interpolar_x),
      y_interp(interpolar_x))

# Vectores para graficas
"""muestras = 100 # Numero cualquiera
a = np.min(X)
b = np.max(X)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)"""

# Gráfica del modelo
plt.plot(X,Y, 'o')
plt.scatter(X, Y, color = 'blue')
#plt.plot(p_X,pfi)
plt.show()