__author__ = 'wemstar'

import matplotlib.pyplot as plt
import numpy as np

N = 1000
M = 100
choice = [-1., 1.]
wynik = []
for n in range(N):
    x = np.random.choice(choice, size=[n, M])
    x = np.sum(x, axis=0)
    wynik.append(np.sqrt(np.mean(x ** 2.0)))
plt.plot(wynik)
plt.plot(np.sqrt(np.arange(len(wynik))))
plt.savefig('zad1.png')
plt.show()
