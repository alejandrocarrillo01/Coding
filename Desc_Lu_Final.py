# Este programa toma la mayoria de los sistemas de ecuaciones de 3 incognitas y las resuelve
# Este codigo no usa pivotes, asi que pueden haber errores con algunas matrices, siempre revisar.
# Hecho por Daniel Alejandro Carrillo

import numpy as np
from scipy.linalg import lu, solve_triangular
# scipy es una biblioteca para realizar soluciones matematicas
# solve_triangular, realiza la solucion de ecuaciones lineales cuando hay upper y lower


while True:
    entrada = input( "ingrese los digitos de la matriz ordenados, separados por una coma. ")
    if len(entrada.split(','))!=9:
        print ("Debes insertar 9 digitos ")
    else:
        entrada = list(map(float, entrada.split(',')))
        A = np.array(entrada).reshape(3,3)
        break

while True:
    entradaresults = input("Ingrese los digitos respuesta desde x hasta z separado por comas. ")
    if len(entradaresults.split(','))!=3: 
        print ("Debes insertar 3 digitos")
    else:
        entradaresults = list(map(float, entradaresults.split(',')))
        b = np.array(entradaresults)
        break

print ("\n")

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
