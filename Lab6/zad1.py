from visual import *
import numpy as np

r = 0.3
a = 4.0
b = 8.
n = 20
scena = display(width=550, height=550)

boxes = [
    box(pos=(a, 0, 0), size=(0.1, b, b), color=color.red),
    box(pos=(-a, 0, 0), size=(0.1, b, b), color=color.green),
    box(pos=(0, a, 0), size=(b, 0.1, b), color=color.blue),
    box(pos=(0, -a, 0), size=(b, 0.1, b), color=color.yellow),
    box(pos=(0, 0, -a), size=(b, b, 0.1), color=color.orange)
]

ballsStartX = (np.random.random_sample(n) - 0.5) * 4
ballsStartY = (np.random.random_sample(n) - 0.5) * 4
ballsStartZ = (np.random.random_sample(n) - 0.5) * 4
kule = []
for x, y, z in zip(ballsStartX, ballsStartY, ballsStartZ):
    kul = sphere(pos=(x, y, z), radius=r, color=color.red)
    kul.pred = np.random.random_integers(-2, 2, 3)
    kule.append(kul)
dt = .1
scena.autoscale = False
while True:
    rate(20)
    for kul in kule:
        kul.pos += kul.pred * dt
        if boxes[0].x <= (kul.x + kul.radius):
            kul.pred[0] = -kul.pred[0]
            kul.color=boxes[0].color
        if boxes[1].x >= (kul.x - kul.radius):
            kul.pred[0] = -kul.pred[0]
            kul.color=boxes[1].color
        if boxes[2].y <= kul.y + kul.radius:
            kul.pred[1] = -kul.pred[1]
            kul.color=boxes[2].color
        if boxes[3].y >= kul.y - kul.radius:
            kul.pred[1] = -kul.pred[1]
            kul.color=boxes[3].color
        if boxes[4].z >= kul.z + kul.radius:
            kul.pred[2] = -kul.pred[2]
            kul.color=boxes[4].color
        if a <= kul.z - kul.radius:
            kul.pred[2] = -kul.pred[2]
