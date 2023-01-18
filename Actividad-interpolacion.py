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

# Se ingresan valores θ start (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([170, 160, 150, 140, 130, 120, 110, 100, 90])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores %of cycle (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([5.6, 11.1, 16.7, 22.2, 27.8, 33.3, 38.9, 44.4, 50])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores Minimum ΔCy % (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.00001, 0.00004, 0.00027, 0.001, 0.004, 0.010, 0.023, 0.047, 0.096])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores ΔV % (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.38, 1.53, 3.48, 6.27, 9.90, 14.68, 20.48, 27.15, 35.31])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [Vx/(L2 ω2)] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([1.436, 1.504, 1.565, 1.611, 1.646, 1.679, 1.702, 1.717, 1.725])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [L1/L2] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [L3/L2] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores ΔX/L2 y ΔΒ proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores Minimum ΔVx % (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.006, 0.0038, 0.106, 0.340, 0.910, 1.885, 3.327, 5.878, 9.299])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores ΔCy % (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.137, 0.274, 0.387, 0.503, 0.640, 0.752, 0.888, 1.067, 1.446])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [Vx/(L2 ω2)] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347, 1.361, 1.374])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [L1/L2] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores [L3/L2] (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Se ingresan valores ΔX/L2 (xi) y ΔΒ (fi) proporcionados en la tabla del ejercicio propuesto
#xi = np.array([0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456])
#fi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])

# Punto en el que se quiere interpolar ΔΒ = 55°
interpolar_x = 55
 
# Resolviendo y buscando la interpolación
y_interp = lagrange(fi, xi)
print("El valor de Y en X = {} es".format(interpolar_x),
      y_interp(interpolar_x))
print(' ')

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

# Presentación de Gráficas
plt.plot(xi,fi, 'o')
plt.plot(p_xi,pfi)
plt.show()