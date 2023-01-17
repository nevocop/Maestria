# INTERPOLACION MECANISMO EN LINEA RECTA DE HOEKEN
# Se importan las librerias necesarias para el algoritmo
# Se importa la interpolación de Langrange del módulo de interpolación de Scipy
from scipy.interpolate import lagrange
# Se importa la librería Numpy con un alias, para hacer los cálculos
import numpy as np
# Se importa la librería Sympy, para desarrollar la forma algebraica del polinomio
import sympy as sym
# Se importa la librería Matplotlib con un alias, para graficas
import matplotlib.pyplot as plt

# Se ingresan valores ΔX/L2 y ΔΒ proporcionados en la tabla del ejercicio propuesto
xi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Conocer la longitud de xi 
n = len(xi)
# Se asigna un carácter x para representar la variable X del polinomio
x = sym.Symbol('x')
# Inicialización del polinomio
polinomio = 0
# Desplazamiento de i dentro del rango xi para encontrar todos los terminos del polinomio
for i in range(0,n,1):
    """ Calculo del primer termino Langrage, es necesario calcular un numerador que se obtiene por multiplicaciones
    Por tal razón se inicializa en "1" tanto numerador y denominador del polinomio"""
    numerador = 1
    denominador = 1
    # El numerador debe recorrer todos los puntos del vector xi
    for j in range(0,n,1):
        # Se condiciona al no uso del punto de referencia y se calcula numerador y denominador
        if (i != j):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
        # Calculo de los terminos de lagrange
        termino = (numerador/denominador)*fi[i]
    # Se acumulan todos los terminos del polinomio
    polinomio = polinomio + termino
    
# Se simplifica el polinomio
polisimple = sym.expand(polinomio)

# Forma lambda (convrsión a forma numerica) del polinomio px, referencia x y el polinomio que se desea convertir
px = sym.lambdify(x, polinomio)

# Vectores para graficas
muestras = 100 # Numero cualquiera que garantice que se van a graficar la cantidad de puntos necesarios
# Valor mínimo del vector
a = np.min(xi)
# Valor máximo del vector
b = np.max(xi)
# Serie de puntos para el trazado de la línea
p_xi = np.linspace(a,b,muestras)
# Se llama el polinomio en forma lambda para el que se requiere la evaluación del polinomio
pfi = px(p_xi)

# Presentación de los polinomios
print('polinomio')
print(polinomio)
print(' ')
print('polinomio simplificado')
print(polisimple)

# Punto en el que se quiere interpolar ΔΒ = 55°
interpolar_x = 55
 
# Resolviendo y buscando la interpolación
y_interp = lagrange(fi, xi)
print("El valor de Y en X = {} es".format(interpolar_x),
      y_interp(interpolar_x))

# Presentación de Gráficas
plt.plot(xi,fi, 'o')
plt.plot(p_xi,pfi)
plt.show()