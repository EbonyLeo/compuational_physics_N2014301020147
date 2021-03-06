from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(10000)

for i in range(100):
    for j in range(10000):
        length = 2*np.random.rand() - 1      
        x_now[j] = x_now[j] + length
    average = sum(x_now)/10000
    x_ave[i+1] = average
    
plt.scatter(steps, x_ave)
plt.plot(steps, x_y0)
plt.xlim(0,100)
plt.ylim(-2,2)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x>')
plt.title('<x> of 10000 walkers, random step length')

plt.show()

