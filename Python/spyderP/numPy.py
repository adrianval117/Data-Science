import numpy as np
import time 
import sys

tamaño= 10000000

print("Vector numpy")
t_vector=time.time()
vector_numpy=np.arange(tamaño, dtype="int64")
suma_vector=vector_numpy.sum()
print("Suma: " + str(suma_vector))
print("Tiempo de ejecución: " + str(time.time()-t_vector))
print("El tamñano de la lista tradicional es: " + str(sys.getsizeof(vector_numpy)/1024**2))

print("--------------------------------------------------")

print("Vector lista tradicional")
t_lista=time.time()
lista=list(range(tamaño))
suma_lista=sum(lista)
print("Suma: " +str(suma_lista))
print("Tiempo de ejecución: " + str(time.time()-t_lista))
print("El tamñano de la lista tradicional es: " + str(sys.getsizeof(lista)/1024**2))

