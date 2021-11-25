import numpy as np
import matplotlib.pyplot as plt 
import random

#operaciones básicas con numpy arrays
vector_a=np.arange(100)
vector_b=np.arange(100)**(1/2)

suma_v=vector_a + vector_b
mult_v=vector_a * vector_b

#Sistema de ecuaciones
A=np.array([[3, 1], [ 4, -3]])
B=np.array([[22], [-1]])
X=np.linalg.solve(A, B)

#Matrices
matriz = np.array([[1, 2], [3, 4]])
suma_mat=matriz.sum() 
prom_mat=matriz.mean()
desv_mat=matriz.std()
cuad_mat=matriz**2
inv_mat=np.linalg.inv(matriz)
det_mat=np.linalg.det(matriz)
mult_inv_mat=np.dot(matriz, inv_mat)

#Ajuste polinómico
x= np.arange(-2,2,0.1)
y = np.array([np.sin(valor * (180/np.pi)) for valor in x])
#plt.plot(x,y)
coefi = np.polyfit(x, y, 12)
y_estimada=np.polyval(coefi, x)
#plt.plot(x, y_estimada)

#Números aleatorios en numpy
n = 100000 

uniforme = np.random.uniform(20, 80, n)
plt.subplot(2, 2, 1)
plt.hist(uniforme, bins=100)

normal=np.random.normal(50, 160, n)
plt.subplot(2, 2, 2)
plt.hist(normal, bins=100, color='red')

triangular = np.random.triangular(20, 30, 80, n)
plt.subplot(2, 2, 3)
plt.hist(triangular, bins=100, color='orange')

exponential = np.random.exponential(100, n)
plt.subplot(2, 2, 4)
plt.hist(exponential, bins=100, color='yellow')
