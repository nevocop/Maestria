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
term = 50

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
print('\nEl coeficiente a0 es: ', an_0)                 # Se imprime el valor del coeficiente (a0)

# Cálculo de coeficientes (an)
Integral = Y * sym.cos(n*W*t)                           # Cálculo de la integral                                           
Integrado = sym.integrate(Integral,(t,t_ini,t_fin))     # Evaluación de la integral entre los límites de la función
an = (2/T) * Integrado                                  # La evaluación de la integral se multiplica por (2/T)
an = sym.simplify(an)                                   # Se utiliza la función simplify para guardar el resultado simplificado
print('\nExpresión an: \n')                             # Impresión de la expresión (an)
sym.pprint(an)                                          # Muestra el resultado de una forma mas ordenada

# Cálculo de coeficientes (bn)
Integral = Y * sym.sin(n*W*t)                           # Cálculo de la integral
Integrado = sym.integrate(Integral,(t,t_ini,t_fin))     # Evaluación de la integral entre los límites de la función
bn = (2/T * Integrado)                                  # La evaluación de la integral se multiplica por (2/T)
bn = sym.simplify(bn)                                   # Se utiliza la función simplify para guardar el resultado simplificado
print('\nExpresión bn: \n')                             # Impresión de la expresión (bn)
sym.pprint(bn)                                          # Muestra el resultado de una forma mas ordenada

# Se evaluan los coeficientes y se colocan en arreglos
a0 = an.subs(n,0)                                       # Inicialización de arreglo en el que se van a mostrar los coeficientes de an
b0 = bn.subs(n,0)                                       # Inicialización de arreglo en el que se van a mostrar los coeficientes de bn
an_ini = [a0] ; bn_ini = [b0]                           # Se almacenan los arreglos en las variables finales
# Inicialización del arreglo donde se muestran la cantidad de coeficientes solicitados
n_i = [0]                                               
i = 1
# Ciclo para recorrer y almacenar los coeficientes en los arreglos creados
while (i<=term):                                        
    avalor = an.subs(n,i)
    bvalor = bn.subs(n,i)
    an_ini.append(avalor)
    bn_ini.append(bvalor)
    n_i.append(i)
    i = i+1

coef_fourier = {'n' : n_i, 'an' :an_ini, 'bn' :bn_ini}  # Se imprimen los coeficientes de Fourier
print('\n Se presentan los coeficientes: \n')
for coef in coef_fourier:
    print(coef, ':', coef_fourier[coef])

# Elaboración de la serie de Fourier
ser_Fou = a0 + 0*t                                      # Se crea la variable donde se almacenará la serie de Fourier
i = 1
# Ciclo para recorrer el arreglo creado y posteriormente mostrar la serie de Fourier
while (i<=term):
    ser_Fou = ser_Fou + an_ini[i]*sym.cos(i*W*t)
    ser_Fou = ser_Fou + bn_ini[i]*sym.sin(i*W*t)
    i = i+1
print('\nLa serie de Fourier para la función dada es:\n') # Se imprime la serie de Fourier
sym.pprint(ser_Fou)                                     # Muestra el resultado de una forma mas ordenada

# Gráfica de la función y de la serie de Fourier
cant_muestras = 150                                     # Número cualquiera para evaluar la gráfica
f_y = sym.lambdify(t,Y)                                 # Uso la función lambdify para transformar valores de la funcion vs tiempo
fs_y = sym.lambdify(t, ser_Fou)                         # Uso la función lambdify para transformar valores de la serie fourie vs tiempo
ti = np.linspace(t_ini, t_fin, cant_muestras)           # Uso la función np.linspace para organizar los datos en un arreglo
fi = f_y(ti)                                            # Se almacenan los resultados para grafica de la función
fsi = fs_y(ti)                                          # Se almaecnana los resultados para grafica de la serie de Fourier

# Se crea la etiqueta de las convenciones y su ubicación en la gráfica
plt.plot(ti,fi,color='red',label = 'f(t)')
plt.plot(ti,fsi,color='green',label = 'términos = '+ str(term))
plt.legend(bbox_to_anchor =(0.75, 0.90))
plt.grid()

# Se nombran el título y los ejes de la gráfica
plt.title('Actividad_Fourier')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo(t)')

# Se crean los puntos sobre los que pasará la gráfica
plt.annotate('-T/2', xy = (np.pi, 0), xytext = (-3.2, -1.10))
plt.annotate('-T/4', xy = (np.pi, 0), xytext = (-1.8, -1.10))
plt.annotate('T/4', xy = (np.pi, 0), xytext = (1.4, -1.10))
plt.annotate('T/2', xy = (np.pi, 0), xytext = (2.9, -1.10))
plt.show()