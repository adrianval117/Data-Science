#GRAFICA DE POTENCIA VS TENSIÓN

from matplotlib import pyplot as plt
import numpy as np

voltaje_init=60
voltaje_end=130
voltaje_step=10

v_t=np.arange(voltaje_init, voltaje_end, voltaje_step)
print(v_t)
a1=0.515
p_v=np.array([a1+0.88, a1+0.90, a1+0.92, a1+0.94, a1+0.95, a1+0.96, a1+0.96])
p_vp=p_v*v_t
print(p_v)

plt.plot(v_t, p_vp)
plt.title('Voltage vs Potencia')
plt.show()


