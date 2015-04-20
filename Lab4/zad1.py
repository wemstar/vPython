import matplotlib.pyplot as plt
import numpy as np

# Ilość kroków czasowych
N = 1000
# Ilośc ścieżek
M = 100
# Wybór ruchu
choice = [-1., 1.]
# Ruch wzdłuż osi X
x = np.random.choice(choice, size=[N, M])
# Ruch wzdłuż osi Y
y = np.random.choice(choice, size=[N, M])

# Położenie w kolejnych krokach czsowych
x = np.cumsum(x, axis=0)
y = np.cumsum(y, axis=0)

# Rysowanie
fig = plt.figure(0.5)
fig.add_subplot(121)
plt.plot(x, y)
fig.add_subplot(122)
plt.plot(x[:, -1], y[:, -1])
plt.savefig('zad1.png')
plt.show()



