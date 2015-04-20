__author__ = 'wemstar'

import matplotlib.pyplot as plt
import numpy as np

# Ilość kroków czasowych
N = 1000
# Ilośc ścierzek
M = 100
# Wybór punktów
choice = [-1., 1.]
wynik = []
# główna pętla
for n in range(N):
    # wybieramy punkty
    x = np.random.choice(choice, size=[n, M])
    # Sumujemy pod koniec ruchu
    x = np.sum(x, axis=0)
    wynik.append(np.sqrt(np.mean(x ** 2.0)))
# plotujemy wynik
plt.plot(wynik)
plt.plot(np.sqrt(np.arange(len(wynik))))
plt.savefig('zad2.png')
plt.show()
