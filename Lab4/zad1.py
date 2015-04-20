import matplotlib.pyplot as plt
import numpy as np

N = 1000
M = 100
choice = [-1., 1.]
x = np.random.choice(choice, size=[N, M])
y = np.random.choice(choice, size=[N, M])
x = np.cumsum(x, axis=0)
y = np.cumsum(y, axis=0)
plt.plot(x, y)
plt.savefig('zad1.png')
plt.show()



