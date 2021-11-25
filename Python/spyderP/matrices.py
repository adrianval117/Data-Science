import numpy as np
import sys

colors=['violeta', 'naranja', 'violeta']
vector_1d=np.array([1, 2, 3, 4, 5])
matriz_2d= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_3d= np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[11, 12, 13],[14, 15, 16],[17, 18, 19]]])

a=(1, 2, 3)
b=(4, 5, 6)
c=tuple([a, b])
print(c)

h="Alfonso"
print(f"El name es {h} ")
print(h[-1])
#colors.pop(1)
#colors.remove('violeta')
#colors.pop()
#colors.insert(0, 'red')
#print(vector_1d[1])
#print(matriz_2d[2,:])
#print(list(range(1,100)))

print(colors)