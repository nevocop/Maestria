"""RESOLUCIÓN DE ECUACIONES CON TRES MÉTODOS NUMÉRICOS
          RUNGE KUTTA, EULER Y EULER MEJORADO"""

# Método Runge Kutta
# Definición de la función runge_kut

def runge_kut(f,x_i,y_i,intervalo,xf):
    y=[y_i]
    x=[x_i]
    h=intervalo
    n=int((xf-x_i)/h)
    for i in range(1,n+1):
        xi = x[i-1]
        yi = y[i-1]
        k1 = f(xi,yi)
        k2 = f(xi+h/2,yi+1/2*h*k1)
        k3 = f(xi+h/2,yi+1/2*h*k2)
        k4 = f(xi+h, yi+h*k3)
        x.append(xi+h)
        y.append(yi+1/6*h*(k1+2*k2+2*k3+k4))
    return x,y

fun_solve = lambda x,y:2*x*y
x,ye=runge_kut(fun_solve,1,1,0.1,1.5)
print(x,ye)
