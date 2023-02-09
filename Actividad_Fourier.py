# SE IMPORTAN LAS LIBRERIAS

# Se importa la libreria sympy para determinar las expresiones de los coeficientes
import sympy as sym
# Se importan las librerias para las gráficas
import numpy as np
import matplotlib.pyplot as plt

# Se ingresa la función a evaluar

t = sym.Symbol('t')
T = 2 * sym.pi
Y = sym.Piecewise((-1,t <-T/2),
                   (-1,t <-T/4),
                   ( 1,t < T/4),
                   (-1,t < T/2),
                   (-1,True),)
# Número de coeficientes que el ejercicio pide
n = 8

# Definición del intervalo a trabajar
t_ini = -T/2 ; t_fin = T/2