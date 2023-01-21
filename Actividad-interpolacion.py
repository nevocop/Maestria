# INTERPOLACION MECANISMO EN LINEA RECTA DE HOEKEN
# Se importan las librerias necesarias para el algoritmo
# Se importa la interpolación de Langrange del módulo de interpolación de Scipy
from scipy.interpolate import lagrange
# Se importa la librería Numpy con un alias, para hacer los cálculos
import numpy as np
# Se importa la librería Matplotlib con un alias, para graficas
import matplotlib.pyplot as plt

# Creación de la función encargada de realizar el cálculo del polinomio de Lagrange
def calculo_polinomio(xi,fi):
    # Calculo de polinomio de lagrange
    p = lagrange(xi,fi)
    print('polinomio de lagrange')
    print(p)
    print(' ')
    #print('Punto en el que se va a evaluar el polinomio')
    y=round(p(55), 5)
    #print(y)

    # Cálculo de los vectores de las gráficas
    muestras = 100 # Numero cualquiera
    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a,b,muestras)
    pfi = p(p_xi)

    # Realización y observación de gráficas
    plt.plot(xi,fi, 'o')
    plt.plot(p_xi,pfi)
    plt.show()
    return y

# Se ingresan valores ΔΒ (xi) y θ start (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('θ start')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([170, 160, 150, 140, 130, 120, 110, 100, 90])
θstart=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y %of cycle (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('Percentage of cycle')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([5.6, 11.1, 16.7, 22.2, 27.8, 33.3, 38.9, 44.4, 50])
porcof_cycle=calculo_polinomio(xi,fi)

# Se ingresan valores Minimum ΔΒ (xi) y ΔCy % (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('Minimum ΔCy %')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.00001, 0.00004, 0.00027, 0.001, 0.004, 0.010, 0.023, 0.047, 0.096])
Minimum_ΔCy=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y ΔV % (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('ΔV %')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.38, 1.53, 3.48, 6.27, 9.90, 14.68, 20.48, 27.15, 35.31])
valores_ΔV=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [Vx/(L2 ω2)] proporcionados en la tabla del ejercicio propuesto
plt.title('[Vx/(L2 ω2)]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([1.436, 1.504, 1.565, 1.611, 1.646, 1.679, 1.702, 1.717, 1.725])
Vx_L2_ω2R=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [L1/L2] (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('[L1/L2]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200])
L1_L2R=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [L3/L2] (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('[L3/L2]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800])
L3_L2R=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y ΔX/L2 (fi) (xi) proporcionados en la tabla del ejercicio propuesto
plt.title('ΔX/L2')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
ΔX_L2R=calculo_polinomio(xi,fi)

# Se ingresan valores Minimum ΔΒ (xi) y ΔVx % (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('Minimum ΔVx %')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.006, 0.0038, 0.106, 0.340, 0.910, 1.885, 3.327, 5.878, 9.299])
Minimum_ΔVx=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y ΔCy % (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('ΔCy %')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.137, 0.274, 0.387, 0.503, 0.640, 0.752, 0.888, 1.067, 1.446])
ΔCy=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [Vx/(L2 ω2)] (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('[Vx/(L2 ω2)]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347, 1.361, 1.374])
Vx_L2_ω2V=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [L1/L2] (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('[L1/L2]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575])
L1_L2V=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y [L3/L2] (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('[L3/L2]')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863])
L3_L2V=calculo_polinomio(xi,fi)

# Se ingresan valores ΔΒ (xi) y ΔX/L2 (fi) proporcionados en la tabla del ejercicio propuesto
plt.title('ΔX/L2')
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456])
ΔX_L2V=calculo_polinomio(xi,fi)

# Cálculo de L1, L2 y L3 para optimización por rectitud
Delta_x = 20
L2R = round(Delta_x/ΔX_L2R, 5)
L1R = round(L1_L2R * L2R, 5)
L3R = round(L3_L2R * L2R, 5)

# Cálculo de L1, L2 y L3 para optimización por rectitud
L2V = round(Delta_x/ΔX_L2V, 5)
L1V = round(L1_L2V * L2V, 5)
L3V = round(L3_L2V * L2V, 5)

#Se imprimen y muestran resultados finales

print('\nVALORES CORRESPONDIENTES A UN ΔΒ = 55°')
print(' ') #Salto de linea
print('OPTIMIZACIÓN POR RECTITUD')
print('\nθ start        ', θstart)
print('porc cycle     ', porcof_cycle)
print('Minimum ΔCy %  ', Minimum_ΔCy)
print('ΔV %           ', valores_ΔV)
print('[Vx/(L2 ω2)]   ', Vx_L2_ω2R)
print('[L1/L2]        ', L1_L2R)
print('[L3/L2]        ', L3_L2R)
print('ΔX/L2          ', ΔX_L2R)
print('L1             ', L1R)
print('L2             ', L2R)
print('L3             ', L3R)
print(' ') #Salto de línea
print('OPTIMIZACIÓN POR VELOCIDAD')
print('\nMinimum ΔVx %  ', Minimum_ΔVx)
print('ΔCy %          ', ΔCy)
print('[Vx/(L2 ω2)]   ', Vx_L2_ω2V)
print('[L1/L2]        ', L1_L2V)
print('[L3/L2]        ', L3_L2V)
print('ΔX/L2          ', ΔX_L2V)
print('L1             ', L1V)
print('L2             ', L2V)
print('L3             ', L3V)