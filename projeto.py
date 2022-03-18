import matplotlib.pyplot as plt
import numpy as np
from numpy import vstack, ones
from numpy.linalg import lstsq

d = int(input("Distancia: "))
h1 = int(input("Altura mastro emissor: "))
h2 = int(input("Altura mastro receptor: "))

x1 = []
y1 = []
with open("cotas.txt",'r') as f:
    for line in f:
        line_sep = line.split(sep=",")
        x1.append(int(line_sep[0]))
        y1.append(float(line_sep[1][:-1]))


RAIO_TERRA = 6378000
ke = 4 / 3
x = np.linspace(0, d, len(x1))

req = ke * RAIO_TERRA
xo = d / 2
yo = (d ** 2) / (8 * req)
y = yo - (((x - xo) ** 2) / (2 * req))

fig, ax = plt.subplots()
ax.plot(x, y, label="Modelo da terra esférica")

y3 = [i + j for i, j in zip(y, y1)]
ax.plot(x, y3, label="Perfil em Terra esférica")

emissor = (0, h1 + y3[0])
receptor = (d, h2 + y3[len(y3) - 1])

ax.plot(emissor[0], emissor[1], marker="o", markersize=10, markerfacecolor="green", label="Emissor")
ax.plot(receptor[0], receptor[1], marker="o", markersize=10, markerfacecolor="red", label="Recetor")

linha_vista = (emissor, receptor)

x_vista = [linha_vista[0][0], linha_vista[1][0]]
y_vista = [linha_vista[0][1], linha_vista[1][1]]
ax.plot(x_vista, y_vista, linestyle="--", label="Linha de vista")

plt.legend()
plt.show()

vista_sim = [int(input("possivel reflexões(x): ")), int(input("possivel reflexões(y): "))]
vista_sim_r = [(vista_sim[0], vista_sim[1]), (receptor[0], receptor[1])]

fig1, ax = plt.subplots()
ax.plot(x, y, label="Modelo da terra esférica")
ax.plot(x, y3, label="Perfil em Terra esférica")
ax.plot(emissor[0], emissor[1], marker="o", markersize=10, markerfacecolor="green", label="Emissor")
ax.plot(receptor[0], receptor[1], marker="o", markersize=10, markerfacecolor="red", label="Recetor")
ax.plot(x_vista, y_vista, linestyle="--", label="Linha de vista")


def line_eq(vista_simultaneo):
    x_coords, y_coords = zip(*vista_simultaneo)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=None)[0]
    print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m * x + c


ax.plot(x, line_eq(vista_sim_r), linestyle="--", label="Zona vista sim.")

plt.legend()
plt.show()

dis = [int(input("Interseção do perfil com a linha de vista mútua(x): ")),
       int(input("Interseção do perfil com a linha de vista mútua(y): "))]

h_linha = emissor[1] - dis[1]

beta = np.arctan((emissor[1] - receptor[1]) / d)
print(f"Beta = {beta} rad")

alfa = np.arctan(h_linha / dis[0])
print(f"Alfa = {alfa} rad")

gamma = alfa - beta
print(f"Gamma = {gamma} rad")

theta = 2 * gamma
print(f"Theta = {theta} rad")

g = (4 * np.pi) / (theta ** 2)
g_dB = 10 * np.log10(g)
print(f"Ganho = {g}\nGanho[dB] = {g_dB} dB")

fig2, ax = plt.subplots()
ax.plot(x, y, label="Modelo da terra esférica")
ax.plot(x, y3, label="Perfil em Terra esférica")
ax.plot(emissor[0], emissor[1], marker="o", markersize=10, markerfacecolor="green", label="Emissor")
ax.plot(receptor[0], receptor[1], marker="o", markersize=10, markerfacecolor="red", label="Recetor")
ax.plot(x_vista, y_vista, linestyle="--", label="Linha de vista")

vista_sim_e = [(vista_sim[0], vista_sim[1]), (emissor[0], emissor[1])]
vista_sim2 = [int(input("possivel reflexões(x): ")), int(input("possivel reflexões(y): "))]
vista_sim_r2 = [(vista_sim2[0], vista_sim2[1]), (receptor[0], receptor[1])]
ax.plot(x, line_eq(vista_sim_r2), linestyle="--", label="Zona vista sim 2r.")
ax.plot(x, line_eq(vista_sim_e), linestyle="--", label="Zona vista sim 2e.")

plt.legend()
plt.show()
