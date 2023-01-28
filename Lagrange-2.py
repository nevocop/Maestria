#importamos la interpolación de Langrange del módulo de interpolación de Scipy
from scipy.interpolate import lagrange
#importamos la librería Matplotlib con un alias
import numpy as np
#importamos la librería Numpy con un alias
import matplotlib.pyplot as plt
#Guardamos los valores de x y f(x) a usar, en vectores
x = [0, 1, 3, 6]
y = [-3, 0, 5, 7]
#Graficamos los valores a interpolar
plt.figure ('1')
plt.plot (x, y, 'x', mew=2, label = 'Datos')
plt.xlabel ("X")
plt.ylabel ("Y")
plt.legend ()
#Obtendremos el polinomio de Lagrange para los puntos dados
p = lagrange (x, y)
#Evaluaremos el polinomio obtenido en un intervalo de [0, 6]
x1 = np.linspace (0, 6, 100)
y1 = p(x1)
z=round(p(1.8), 3)
print(z)
#Graficamos el polinomio obtenido así como los puntos usados
plt.figure ('2')
plt.plot (x1, y1, label = 'interpolacion')
plt.plot (x, y, 'x', mew=2, label = 'Datos')
plt.xlabel ("X")
plt.ylabel ("Y")
plt.legend ()
plt.show()