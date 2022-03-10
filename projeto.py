import matplotlib.pyplot as plt
import numpy as np

d = int(input("Distancia: "))
h1 = int(input("Altura mastro emissor: "))
h2 = int(input("Altura mastro receptor: "))

RAIO_TERRA = 6378000
ke = 4/3
x = np.linspace(0, d, 10)
print(x)

req = ke*RAIO_TERRA
xo = d/2
yo = (d**2)/(8*req)
y = yo - (((x-xo)**2)/(2*req))

x1 = [0, 8000, 15000, 21600, 21000, 30600, 40000, 45000, 47600, 50000]
y1 = [97, 45, 25, 31, 13, 0, 0, 0, 27, 20]

fig, ax = plt.subplots()
ax.plot(x, y)

y3 = [i + j for i, j in zip(y, y1)]
ax.plot(x, y3)

plt.plot(0, h1+y3[0], marker="o", markersize=10,  markerfacecolor="green")
plt.plot(d, h2+y3[9], marker="o", markersize=10,  markerfacecolor="green")

plt.show()
