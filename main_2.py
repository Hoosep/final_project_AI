from dataset.tune import CreatePopulation

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.ticker as mticker

from dataset.variables import STATES, YEARS, DATA

fig = plt.figure(figsize=(8, 20))
#fig.set_size_inches(18.5, 10.5)
fig.suptitle('Accidentes Fatales 2014-2019', fontsize=20)

ax = fig.add_subplot(2, 2, 1, projection='3d')
ax_ga = fig.add_subplot(2, 2, 2, projection='3d')
error_ax = fig.add_subplot(2, 2, (3, 4))
# ax = plt.axes(projection="3d")

x = np.arange(len(STATES))
y = np.arange(len(YEARS))

X_REAL, Y_REAL = np.meshgrid(x, y)
Z_REAL = np.array(DATA)


ax.plot_wireframe(X_REAL, Y_REAL, Z_REAL, color='green')
ax.plot_surface(X_REAL, Y_REAL, Z_REAL, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')

ax.set_xticks(range(len(STATES)))
ax.set_xticklabels(STATES)

ax.set_yticks(range(len(YEARS)))
ax.set_yticklabels(YEARS)

ax.set_zlabel('Total')


list_z, errors = CreatePopulation()

length = len(list_z)

x_values = []
for i in range(length):
    Z_DATA = np.array(list_z[i])

    ax_ga.plot_wireframe(X_REAL, Y_REAL, Z_DATA, color='green')
    ax_ga.plot_surface(X_REAL, Y_REAL, Z_DATA, rstride=1, cstride=1,
                    cmap='winter', edgecolor='none')

    ax_ga.set_xticks(range(len(STATES)))
    ax_ga.set_xticklabels(STATES)

    ax_ga.set_yticks(range(len(YEARS)))
    ax_ga.set_yticklabels(YEARS)

    ax_ga.set_zlabel('Total')
    
    x_values.append(i + 1)
    error_ax.plot(x_values, errors[:i + 1], '-', color='green', label='Precipitacion - GA')


    plt.pause(0.01)
    ax_ga.cla()
    error_ax.cla()
    



Z_DATA_LAST = np.array(list_z[41])

ax_ga.plot_wireframe(X_REAL, Y_REAL, Z_DATA_LAST, color='green')
ax_ga.plot_surface(X_REAL, Y_REAL, Z_DATA_LAST, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')

ax_ga.set_xticks(range(len(STATES)))
ax_ga.set_xticklabels(STATES)

ax_ga.set_yticks(range(len(YEARS)))
ax_ga.set_yticklabels(YEARS)

ax_ga.set_zlabel('Total')

error_ax.plot(x_values, errors, '-', color='red')
plt.ioff()
plt.show()