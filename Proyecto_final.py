"""RESOLUCIÓN DE ECUACIONES CON TRES MÉTODOS NUMÉRICOS
          RUNGE KUTTA, EULER Y EULER MEJORADO"""

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

fun_solve = lambda x,y:2*x*y
x,ye=euler_mej(fun_solve,1,1,0.1,1.5)
print(x,ye)

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


