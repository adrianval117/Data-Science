import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

#Variables and interval
L = np.pi
x = np.linspace(-L, L, 1000)
t = sym.Symbol('t')
n = sym.Symbol('n')

#Enter data
ft = t  #<-------- Introduce the function
N = 5             #<-------- Introduce how many harmonics you want

# Find a_0
a_0 = (1/L)*sym.integrate(ft,(t, -L, L))
a_0 = sym.simplify(a_0)

#Find a_n
ft_a_n = ft*sym.cos(n*np.pi*t/L)
a_n = (1/L)*sym.integrate(ft_a_n,(t, -L, L))
a_n = sym.simplify(a_n)

#Find b_n
ft_b_n = ft*sym.sin(n*np.pi*t/L)
b_n = (1/L)*sym.integrate(ft_b_n,(t, -L, L))
b_n = sym.simplify(b_n)

#Set suma = a_0 (DC condition)
suma = a_0/2
aki = 0
bki = 0

#Defining the serie and modeling the functions to plot
for i in range(1, N):
    aki = a_n.subs(n, i)
    bki = b_n.subs(n, i)
    suma += aki*np.cos(i*np.pi*x/L) + bki*np.sin(i*np.pi*x/L)
fx = []
for point in x:
    fx = np.append(fx, ft.subs(t, point))

#Plotting serie and function
plt.figure(figsize=(5.69, 3.47))
plt.plot(x, fx, label = 'f(t)', color='b')
plt.plot(x, suma, label = 'Harmonics = '+ str(N), color='r')
plt.subplots_adjust(bottom=0.25)
ax = plt.gca()
ax.legend()
ax.set_xlabel('t')
ax.set_ylabel('Amplitude')
ax.set_title('Fourier Series: Original Vs. Aproximation')
plt.show()