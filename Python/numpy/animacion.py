import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 

fig, ax = plt.subplots()
fig.set_tight_layout(True)

x = np.linspace(0, 1.00, 100)
ax.plot(x, np.sin(2*np.pi*x))
line, = ax.plot(x, np.sin(2*np.pi*x), 'r-', linewidth=2)

def update(i):
    line.set_ydata((1+i)*np.sin(2*np.pi*x))

anim = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, 2*np.pi, 0.01), interval=1)
plt.show()