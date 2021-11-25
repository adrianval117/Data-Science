# Graficas de funciones singulares
from matplotlib import pyplot as plt
import numpy as np
from sympy import *

# funcion escalon unitario
def u(t): 
    return np.piecewise(t,[t<0.0,t>=0.0],[0,1])

# funcion f(t)
def f(t): 
    return np.exp(-2*t)*u(t)
 
t=np.linspace(-1,5,1000)
plt.xlim(-1.5,5.5)
plt.ylim(0,1.2)
plt.plot(t,f(t),'k',label=r'$f(t)$',lw=2)
plt.legend(loc='best')
plt.title('Function')
