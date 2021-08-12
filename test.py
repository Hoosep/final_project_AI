from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from dataset.variables import STATES, YEARS, DATA


def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
ax = plt.axes(projection="3d")

x = np.arange(len(STATES))
y = np.arange(len(YEARS))


X, Y = np.meshgrid(x, y)
Z = np.array(DATA)

ax.plot_wireframe(X, Y, Z, color='green')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_title('Accidentes Fatales 2014-2019')

ax.set_xticks(range(len(STATES)))
ax.set_xticklabels(STATES)

ax.set_yticks(range(len(YEARS)))
ax.set_yticklabels(YEARS)


ax.set_zlabel('Total')

plt.show()