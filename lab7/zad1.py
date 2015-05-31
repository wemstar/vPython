__author__ = 'wemstar'
import visual as vs
import numpy as np


def calculateVelocities(k1, k2):
    a=vs.mag((k1.vel-k2.vel)**2.0)
    b=-2.*np.dot((k1.pos-k2.pos),(k1.vel-k2.vel))
    c=vs.mag(np.power(k1.pos-k2.pos,2.)-np.power(k1.radius+k2.radius,2.))
    delta=b**2.0-4.0*a*c
    if a == 0. or delta < 0.:
        return
    dtp=(-1.0*b+np.sqrt(delta))/(2.*a)
    k1.pos-=k1.vel*dtp
    k2.pos-=k2.vel*dtp
    wsp=(k1.pos-k2.pos)/(np.abs(vs.mag(k1.pos-k2.pos)))
    k1.vel=k1.vel-2.0* k2.m /(k1.m+k2.m)*np.dot(k1.vel-k2.vel,wsp)*wsp
    k2.vel=k2.vel+2.0* k2.m /(k1.m+k2.m)*np.dot(k1.vel-k2.vel,wsp)*wsp
    k1.pos+=k1.vel*dtp
    k2.pos+=k2.vel*dtp
    print("hura")




n = 20
r = 1.
dt = 0.1
kule = []
scena = vs.display(width=550,height=550)
vs.sphere(pos=(0, 0, 0), radius=20,opacity=0.1)
for x in range(n):
    kula = vs.sphere(pos=np.random.randint(-5,5,3), radius=r)
    kula.m=1.
    kula.vel = np.random.randint(-5,5,3)
    kule.append(kula)

while True:
    vs.rate(10)
    for k1 in kule:
        for k2 in kule:
            k1.pos += k1.vel * dt
            if np.abs(vs.mag(k1.pos - k2.pos)) <= 3.0 * r:

                calculateVelocities(k1, k2)
            if np.abs(vs.mag(k1.pos)) > 20.:
                k1.vel = -k1.vel

