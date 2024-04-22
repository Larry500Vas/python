from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.arange(0, 6, 0.25)
Y = np.arange(0, 6, 0.25)
X, Y = np.meshgrid(X, Y)

Z1 = np.empty_like(X)
Z2 = np.empty_like(X)
C1 = np.empty_like(X, dtype=object)
C2 = np.empty_like(X, dtype=object)

for i in range(len(X)):
    for j in range(len(X[0])):
        z1 = 0.5 * (erf((X[i, j] + Y[i, j] - 4.5) * 0.5) + 1)
        z2 = 0.5 * (erf((-X[i, j] - Y[i, j] + 4.5) * 0.5) + 1)
        Z1[i, j] = z1
        Z2[i, j] = z2
        C1[i, j] = plt.get_cmap("Oranges")(z1)
        C2[i, j] = plt.get_cmap("Blues")(z2)

X_bridge = np.vstack([X[-1, :], X[-1, :]])
Y_bridge = np.vstack([Y[-1, :], Y[-1, :]])
Z_bridge = np.vstack([Z1[-1, :], Z2[-1, :]])
color_bridge = np.empty_like(Z_bridge, dtype=object)
color_bridge.fill((1, 1, 1, 0))

X_full = np.vstack([X, X_bridge, np.flipud(X)])
Y_full = np.vstack([Y, Y_bridge, np.flipud(Y)])
Z_full = np.vstack([Z1, Z_bridge, np.flipud(Z2)])
color_full = np.vstack([C1, color_bridge, np.flipud(C2)])

surf_full = ax.plot_surface(X_full, Y_full, Z_full, rstride=1, cstride=1,
                             facecolors=color_full, linewidth=0,
                             antialiased=False)

plt.show()

