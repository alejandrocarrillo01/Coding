import numpy as np
from scipy.linalg import lu, solve_triangular
# scipy es una biblioteca para realizar soluciones matematicas
# solve_triangular, realiza la solucion de ecuaciones lineales cuando hay upper y lower

A = np.array([[1, 7, -4],
              [4, -4,9],
              [12, -1, 3]], dtype=float)

# Este el vector del otro lado del igual 
b = np.array([-51,62,8], dtype=float)

#Debemos guardar los operando para la matriz Lower  
operando1=(A[1,0]/A[0,0])
# Y hacemos la operacion 
fila2=A[1]- (operando1*A[0])
A[1,:]=fila2

# Repetimos y actualizamos la matriz 
operando2=(A[2,0]/A[0,0])
fila3= A[2]-(operando2*A[0])
A[2,:]=fila3

# Y repetimos con el ultimo 0 
operando3=(A[2,1])/A[1,1]
fila3= A[2]-(operando3*A[1])
A[2,:]=fila3

#Creamos lower usando los operandos 
Lower = np.array([[1,0,0],
             [operando1,1,0],
             [operando2,operando3,1]])

# Upper ya la tenemos 
Upper = A

# Usamos el metodo solve triangular para sustituir hacia adelante por eso
# "lower=True" eso le dice que solucione hacia adelante 
y = solve_triangular(Lower, b, lower=True)
# Y luego solucionamos hacia atras, para hallar la respuesta.
x = solve_triangular(Upper,y)

# imprimimos usando 4 decimales 

print ("x = ", f"{x[0]:.4f}")
print("y = ", f"{x[1]:.4f}")
print ("z = ", f"{x[2]:.4f}")
