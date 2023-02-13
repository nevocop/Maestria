# SE IMPORTAN LAS LIBRERIAS

# Se importa la libreria sympy para determinar las expresiones de los coeficientes
import sympy as sym
# Se importan las librerias para las gráficas
import numpy as np
import matplotlib.pyplot as plt


t = sym.Symbol('t')                                     # Asignación de símbolo o string a la variable t
T = 6                                                   # Se define el periodo de la función

# Se ingresa la función a evaluar
Y = sym.Piecewise((-1,t <-T/4),                         # Se utiliza Piecewise para crear la función a graficar
                   ( 1,t < T/4),
                   (-1,t < T/2),
                   (-1,True),)

# Número de coeficientes que pide el ejercicio
n = 8

# Procedimiento para calcular la Serie de Fourier
# Definición del intervalo en el cual se va a analizar la función
t_ini = -T/2 ; t_fin = T/2
n = sym.Symbol('n')                                     # Asignación de símbolo o string a la variable n
W = 2*sym.pi/T                                          # Definición de la frecuencia de la función

# Cálculo del coeficiente (a0)
Integral = Y                                            # Cálculo de la integral
Integrado = sym.integrate(Integral,(t,t_ini,t_fin))     # Evaluación de la integral entre los límites de la función
an_0 = (2/T)*Integrado                                  # La evaluación de la integral se multiplica por (2/T)
an_0 = sym.simplify(an_0)                               # Se utiliza la función simplify para guardar el resultado simplificado
print('\nEl coeficiente a0 es: ', an_0)                # Se imprime el valor del coeficiente (a0)

# Cálculo de coeficientes (an)
Integral = Y * sym.cos(n*W*t)                           # Cálculo de la integral                                           
Integrado = sym.integrate(Integral,(t,t_ini,t_fin))     # Evaluación de la integral entre los límites de la función
an = (2/T) * Integrado                                  # La evaluación de la integral se multiplica por (2/T)
an = sym.simplify(an)                                   # Se utiliza la función simplify para guardar el resultado simplificado
print('\nExpresión an: \n')                               # Impresión de la expresión (an)
sym.pprint(an)