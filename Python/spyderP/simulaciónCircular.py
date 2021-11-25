import random
import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n):
    circle_points=0
    total_points=0
    for i in range(n):
        x=random.uniform(0, 1)
        y=random.uniform(0, 1)
        distance=x**2+y**2
        if distance<=1:
            circle_points+=1
        total_points+=1
    xcircle=np.arange(0, 1, 0.01)
    ycircle=(1-xcircle**2)**(1/2)
    plt.plot(xcircle, ycircle)
    x=np.random.uniform(0, 1, n)
    y=np.random.uniform(0, 1, n)
    x1, x2, y1, y2=np.array([]), np.array([]), np.array([]), np.array([])
    for i in range(len(x)):
        for i in range(len(y)):
            distance=x[i]**2+y[i]**2
            if distance <=1:
                x1=np.append(x1, [x[i]])
                y1=np.append(y1, [y[i]])
            else:
                x2=np.append(x2, [x[i]])
                y2=np.append(y2, [y[i]])
    plt.scatter(x1, y1, s=10, c='b', edgecolors='b')
    plt.scatter(x2, y2, s=10, c='r', edgecolors='r')
    plt.gca().set_aspect('equal')
    plt.show()
    return 4*circle_points/total_points


