import matplotlib.pyplot as plt
import numpy as np
from numpy import vstack, ones
from numpy.linalg import lstsq

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

vista_sim = [int(input("possivel reflexões(x): ")), int(input("possivel reflexões(y): "))]
vista_sim_ = [(vista_sim[0], vista_sim[1]), (receptor[0], receptor[1])]


fig1, ax = plt.subplots()
ax.plot(x, y, label="Modelo da terra esférica")
ax.plot(x, y3, label="Perfil em Terra esférica")
ax.plot(emissor[0], emissor[1], marker="o", markersize=10,  markerfacecolor="green", label="Emissor")
ax.plot(receptor[0], receptor[1], marker="o", markersize=10,  markerfacecolor="red", label="Recetor")
ax.plot(x_vista, y_vista, linestyle="--", label="Linha de vista")


x_coords, y_coords = zip(*vista_sim_)
A = vstack([x_coords, ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
y4 = m*x+c
ax.plot(x, y4, linestyle="--", label="Zona vista sim.")

plt.legend()
plt.show()

dis = [int(input("Interseção do perfil com a linha de vista mútua(x): ")),
       int(input("Interseção do perfil com a linha de vista mútua(y): "))]

h_linha = emissor[1]-dis[1]

beta = np.arctan((emissor[1]-receptor[1])/d)
print(f"Beta = {beta} rad")

alfa = np.arctan(h_linha/dis[0])
print(f"Alfa = {alfa} rad")

gamma = alfa-beta
print(f"Gamma = {gamma} rad")

theta = 2*gamma
print(f"Theta = {theta} rad")
g = (4*np.pi)/(theta**2)
g_dB = 10*np.log10(g)
print(f"Ganho = {g}\nGanho[dB] = {g_dB} dB")
