"""RESOLUCIÓN DE ECUACIONES DE PRIMER ORDE, CON TRES MÉTODOS 
        NUMÉRICOS RUNGE KUTTA, EULER Y EULER MEJORADO"""

# Se importan las librerias necesarias para el Programa

import matplotlib.pyplot as plt                         # librería para graficar los tres métodos
import pandas as pd                                     # librería para el manejo de tablas
from math import *                                      # librería para calculos matemáticos
# MÉTODO DE EULER
# Definición de la función Euler

def euler(f,x_i,y_i,intervalo,xf):                      # Definición de la función con sus respectivos parámetros
    x=[x_i]                                             # Se crea la lista donde se almacenarán los valores de x
    y=[y_i]                                             # Se crea la lista donde se almacenarán los valores de y    
    h=intervalo                                         # Se crea la variable donde se almacena el intervalo a usar
    n=int((xf-x_i)/h)                                   # Número de iteraciones que se ralizarán para resolver la ecuación
    
    # Se crea ciclo for para resolver la ecuación por el método de Euler
    for i in range(1,n+1):
        xi = x[i-1]                                     # Inicialización de la lista para x
        yi = y[i-1]                                     # Inicialización de la lista para y
        
        # Se aplica la fórmula para método numérico de Euler
        x_euler = xi+h
        y_euler = yi+h*f(xi,yi)
        x.append(x_euler)                               # Se agregan términos a la lista x
        y.append(y_euler)                               # Se agregan términos a la lista y
    return x,y

# MÉTODO DE EULER MEJORADO
# Definición de la función Euler Mejorado

def euler_mej(f,x_i,y_i,intervalo,xf):                  # Definición de la función con sus respectivos parámetros
    x=[x_i]                                             # Se crea la lista donde se almacenarán los valores de x
    y=[y_i]                                             # Se crea la lista donde se almacenarán los valores de y    
    h=intervalo                                         # Se crea la variable donde se almacena el intervalo a usar
    n=int((xf-x_i)/h)                                   # Número de iteraciones que se ralizarán para resolver la ecuación
    
    # Se crea ciclo for para resolver la ecuación por el método de Euler Mejorado
    for i in range (1, n+1):        
        xi = x[i-1]                                     # Inicialización de la lista para x
        yi = y[i-1]                                     # Inicialización de la lista para y
        
        # Se aplica la fórmula para método numérico de Euler Mejorado
        yim = yi + h*f(xi,yi)
        yi = yi + h/2*(f(xi+h,yim)+f(xi,yi))
        x.append(xi+h)                                  # Se agregan términos a la lista x
        y.append(yi)                                    # Se agregan términos a la lista y
    return x,y

# METODO DE RUNGE KUTTA
# Definición de la función runge_kut

def runge_kut(f,x_i,y_i,intervalo,xf):                  # Definición de la función con sus respectivos parámetros
    x=[x_i]                                             # Se crea la lista donde se almacenarán los valores de x
    y=[y_i]                                             # Se crea la lista donde se almacenarán los valores de y    
    h=intervalo                                         # Se crea la variable donde se almacena el intervalo a usar
    n=int((xf-x_i)/h)                                   # Número de iteraciones que se ralizarán para resolver la ecuación
    
    # Se crea ciclo for para resolver la ecuación de acuerdo al método Range Kutta
    for i in range(1,n+1):
        xi = x[i-1]                                     
        yi = y[i-1]

        # Cálculo de las pendientes necesarias para el Método Runge Kutta

        k1 = f(xi,yi)                                   
        k2 = f(xi+h/2,yi+h/2*k1)
        k3 = f(xi+h/2,yi+h/2*k2)
        k4 = f(xi+h, yi+h*k3)
        x.append(xi+h)                                  # Se agregan términos a la lista x
        y.append(yi+h/6*(k1+2*k2+2*k3+k4))              # Se agregan términos a la lista y
    return x,y

# Solicitud de datos para analizar

funcion = input("Ingrese la función: ")                 # Se crea la variable donde se almacenará la función a resolver
x_i = float(input("Ingrese valor inicial de x: "))      # Se ingresa el valor inicial de x
y_i = float(input("Ingrese el valor inicial de y: "))   # Se ingresa el valor inicial de y
y_f = float(input("Ingrese el valor final de y: "))     # Se ingresa el valor final de y
h = float(input("Ingrese el intervalo que se va a utilizar: "))     # Se ingresa el intervalo que se va a utilizar para el análisis
print('\n')                                             # Salto de línea
fun_solve = lambda x,y:eval(funcion)                    # Se ingresa en una variable la función ingresada por el usuario y se evalua
x,ye = euler(fun_solve,x_i,y_i,h,y_f)                   # Se aplica el método de Euler
x,yem = euler_mej(fun_solve,x_i,y_i,h,y_f)              # Se aplica el método de Euler mejorado
x,yrk = runge_kut(fun_solve,x_i,y_i,h,y_f)              # Se aplica el método de Runge Kutta

# Se grafican las curvas de cada uno de los métodos utilizados en el programa
plt.plot(x,ye,".-",label="Euler")
plt.plot(x,yem,".-",label="Euler Mejorado")
plt.plot(x,yrk,".-",label="RGK4")

# Nomenclatura de la gráfica
plt.title("Curvas de solución de los métodos utilizados")   # Se coloca título de la gráfica
plt.legend(loc=4)                                           # Posición del título
plt.xlabel("Eje X")                                         # Se nombra el eje X
plt.ylabel("Eje Y")                                         # Se nombra el eje Y
plt.grid()                                                  # Se coloca cuadrícula en el fondo de la gráfica                                             

# Se crea tabla de valores de las tres soluciones
df=pd.DataFrame(zip(x,ye,yem,yrk),columns=["x","Euler","Euler_Mej","RGK4"])     # Se genera y almacena la tabla en una variable
print(df)                                                   # Se muestra la tabla en pantalla
plt.show()                                                  # Se muestra la gráfica con las tres curvas