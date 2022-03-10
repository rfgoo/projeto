import matplotlib.pyplot as plt
import numpy as np

d = int(input("Distancia: "))
h1 = int(input("Altura mastro emissor: "))
h2 = int(input("Altura mastro receptor: "))

# TODO meter as cotas num txt e ler para o x1 e y1

x1 = [0, 8000, 15000, 21600, 21000, 30600, 40000, 45000, 47600, 50000]
y1 = [97, 45, 25, 31, 13, 0, 0, 0, 27, 20]


RAIO_TERRA = 6378000
ke = 4/3
x = np.linspace(0, d, len(x1))

req = ke*RAIO_TERRA
xo = d/2
yo = (d**2)/(8*req)
y = yo - (((x-xo)**2)/(2*req))


fig, ax = plt.subplots()
ax.plot(x, y, label="Modelo da terra esférica")

y3 = [i + j for i, j in zip(y, y1)]
ax.plot(x, y3, label="Perfil em Terra esférica")

emissor = (0, h1+y3[0])
receptor = (d, h2+y3[len(y3)-1])

ax.plot(emissor[0], emissor[1], marker="o", markersize=10,  markerfacecolor="green", label="Emissor")
ax.plot(receptor[0], receptor[1], marker="o", markersize=10,  markerfacecolor="red", label="Recetor")


linha_vista = (emissor, receptor)

x_vista = [linha_vista[0][0], linha_vista[1][0]]
y_vista = [linha_vista[0][1], linha_vista[1][1]]
ax.plot(x_vista, y_vista, linestyle="--", label="Linha de vista")

plt.legend()
plt.show()
