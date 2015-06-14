import visual as vs
import numpy as np

L = 10.
g = 9.98
m = 1.
r = 1.
fi = np.pi - 0.1
omega = 0.
fiv = 0.
omegav = 0.
scena = vs.display(width=550, height=550)

dt = 0.001
vs.sphere(pos=(0, 0, 0), radius=r, color=vs.color.green)
kula1 = vs.sphere(pos=(L * np.sin(fi), L * np.cos(fi), 0), radius=r, color=vs.color.red)
kula2 = vs.sphere(pos=(L * np.sin(fi) + L * np.sin(omega), L * np.cos(fi) + np.cos(omega), 0), radius=r,
                  color=vs.color.blue)
while True:
    vs.rate(1000)
    fia = (-g / L * (2. * np.sin(fi) - np.sin(omega) * np.cos(fi - omega))
           - 0.5 * (fi ** 2.) * np.sin(2. * fi - 2. * omega)
           - (omega ** 2.0) * np.sin(fi - omega)) \
          / (1. + np.sin(fi - omega) ** 2.)
    omegaa = (-g / L * (2. * np.sin(omega) - 2. * np.sin(fi) * np.cos(fi - omega))
              + 0.5 * (omega ** 2.) * np.sin(2. * fi - 2. * omega)
              + 2.0 * (fi ** 2.0) * np.sin(fi - omega)) \
             / (1. + np.sin(fi - omega) ** 2.)

    fiv = fiv + fia * dt
    omegav = omegav + omegaa * dt
    fi = fi + fia * dt
    omega = omega + omegav * dt

    kula1.x = L * np.sin(fi)
    kula1.y = L * np.cos(fi)
    kula2.x = L * np.sin(fi) + L * np.sin(omega)
    kula2.y = L * np.cos(fi) + L * np.cos(omega)
    print(fi, omega)
