import numpy as np


def urodziny(n):
    ilosc = 10000
    for i in range(2, n):
        licznik = 0
        for j in range(ilosc):
            dni = np.random.choice(np.linspace(1, 365, 365), i)
            macierz = dni == dni[:, np.newaxis]
            macierz = macierz - np.identity(i)
            if 1 in macierz:
                licznik += 1
        yield float(licznik) / ilosc


for i, z in enumerate(urodziny(365)):
    print("{1} {0:0.10f} ".format(z, i + 2))




