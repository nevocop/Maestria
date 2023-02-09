import numpy as np
import matplotlib.pylab as plt

from scipy import signal as sp
# Importamos todo el modulo sympy
from sympy import *
# Importamos las variables simbolicas 'n' y 't'
from sympy.abc import n, t
# Periodo
T = pi
# Frecuencia angular
w = (2*pi)/T

amplitude = 1
time = np.arange(-1, 10, 0.001)
squareWaveFunction = (sp.square(2*time) * amplitude/2.0) + amplitude/2.0

# Graficamos la onda cuadrada
plt.plot(time, squareWaveFunction, lw=2)
plt.grid()
plt.annotate('T', xy = (np.pi, 0), xytext = (np.pi, -0.01))
plt.annotate('T/2', xy = (np.pi / 2.0, 0), xytext = (np.pi / 2.0, 1.01))
plt.ylabel('Amplitude')
plt.xlabel('time(t)')
plt.show()
