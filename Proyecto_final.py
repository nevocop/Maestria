"""RESOLUCIÓN DE ECUACIONES CON TRES MÉTODOS NUMÉRICOS
          RUNGE KUTTA, EULER Y EULER MEJORADO"""

# Método Runge Kutta
# Definición de la función runge_kut

def runge_kut(f,x_i,y_i,intervalo,xf):                  # Definición de la función con sus respectivos parámetros
    x=[x_i]                                             # Se crea la lista donde se almacenarán los valores de x
    y=[y_i]                                             # Se crea la lista donde se almacenarán los valores de y    
    h=intervalo                                         # Se crea la variable donde se almacena el intervalo a usar
    n=int((xf-x_i)/h)                                   # Número de iteraciones que se ralizarán para resolver la ecuación
    
    # Se crea ciclo for para resolver la ecuación de acuerdo al método elegido
    for i in range(1,n+1):
        xi = x[i-1]                                     
        yi = y[i-1]

        # Cálculo de las pendientes

        k1 = f(xi,yi)                                   
        k2 = f(xi+h/2,yi+h/2*k1)
        k3 = f(xi+h/2,yi+h/2*k2)
        k4 = f(xi+h, yi+h*k3)
        x.append(xi+h)                                  # Se agregan términos a la lista x
        y.append(yi+h/6*(k1+2*k2+2*k3+k4))              # Se agregan términos a la lista y
    return x,y

fun_solve = lambda x,y:2*x*y
x,ye=runge_kut(fun_solve,1,1,0.1,1.5)
print(x,ye)
