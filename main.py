from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.ticker as mticker
from math import exp
from sko.GA import GA

from dataset.variables import STATES, YEARS, DATA

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
fig.suptitle('Accidentes Fatales 2014-2019', fontsize=20)

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax_ga = fig.add_subplot(1, 2, 2, projection='3d')
# ax = plt.axes(projection="3d")

x = np.arange(len(STATES))
y = np.arange(len(YEARS))


X_REAL, Y_REAL = np.meshgrid(x, y)
# print("X_REA", X_REAL)
Z_REAL = np.array(DATA)

ax.plot_wireframe(X_REAL, Y_REAL, Z_REAL, color='green')
ax.plot_surface(X_REAL, Y_REAL, Z_REAL, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')

ax.set_xticks(range(len(STATES)))
ax.set_xticklabels(STATES)

ax.set_yticks(range(len(YEARS)))
ax.set_yticklabels(YEARS)

ax.set_zlabel('Total')

###### GA START HERE

x_np = np.array(x)
y_np = np.array(y)


def my_function_ga(x, y, m1, m2, m3, m4, m5, m6, de1, de2, de3, de4, de5, de6, p1, p2, p3, p4, p5, p6, p7, p8, p9, q1, q2, q3, q4, q5, q6, q7, q8, q9, r1, r2, r3, r4, r5, r6, r7, r8, r9):
    mf1 = []
    mf2 = []
    mf3 = []

    mf4 = []
    mf5 = []
    mf6 = []

    index = 1
    a = []
    b = []

    ## CREATE ARRAY 2Dimensional
    z = np.zeros(shape=(6, 6))


    rows, cols = (6, 6)
    arr = [[0]*cols]*rows
    for i in x:
        for j in y:
            a.insert(i, (i + 1) / 6) # This a is my virtual X
            b.insert(j, (j + 1) / 6) # This b is my virtual Y
            
            mf1.insert(i, exp( (-(a[i] - m1) ** 2) / ( 2 * de1 ** 2)  ))
            mf2.insert(i, exp( (-(a[i] - m2) ** 2) / ( 2 * de2 ** 2)  ))
            mf3.insert(i, exp( (-(a[i] - m3) ** 2) / ( 2 * de3 ** 2)  ))
            
            mf4.insert(j, exp( (-(b[j] - m4) ** 2) / ( 2 * de4 ** 2)  ))
            mf5.insert(j, exp( (-(b[j] - m5) ** 2) / ( 2 * de5 ** 2)  ))
            mf6.insert(j, exp( (-(b[j] - m6) ** 2) / ( 2 * de6 ** 2)  ))

            inf1 = mf1[i] * mf4[j]
            inf2 = mf1[i] * mf5[j]
            inf3 = mf1[i] * mf6[j]
            inf4 = mf2[i] * mf4[j]
            inf5 = mf2[i] * mf5[j]
            inf6 = mf2[i] * mf6[j]
            inf7 = mf3[i] * mf4[j]
            inf8 = mf3[i] * mf5[j]
            inf9 = mf3[i] * mf6[j]
        
            reg1 = inf1 * ( p1 * a[i] + q1 * b[j] + r1 )
            reg2 = inf2 * ( p2 * a[i] + q2 * b[j] + r2 )
            reg3 = inf1 * ( p3 * a[i] + q3 * b[j] + r3 )
            reg4 = inf1 * ( p4 * a[i] + q4 * b[j] + r4 )
            reg5 = inf1 * ( p5 * a[i] + q5 * b[j] + r5 )
            reg6 = inf1 * ( p6 * a[i] + q6 * b[j] + r6 )
            reg7 = inf1 * ( p7 * a[i] + q7 * b[j] + r7 )
            reg8 = inf1 * ( p8 * a[i] + q8 * b[j] + r8 )
            reg9 = inf1 * ( p9 * a[i] + q9 * b[j] + r9 )

            d = inf1 + inf2 + inf3 + inf4 + inf5 + inf6 + inf7 + inf8 + inf9
            c = reg1 + reg2 + reg3 + reg4 + reg5 + reg6 + reg7 + reg8 + reg9
            ## UPDATE ARRAY 2Dimensional
            arr[i][j] = int(c / d)
    #print('-'*50)
    #z = z.tolist()
    #print(z)
    return arr

def ga_fun(p):
    #a, b, c, d, e, f, g, h, i, j, k, m = p
    m1, m2, m3, m4, m5, m6, de1, de2, de3, de4, de5, de6, p1, p2, p3, p4, p5, p6, p7, p8, p9, q1, q2, q3, q4, q5, q6, q7, q8, q9, r1, r2, r3, r4, r5, r6, r7, r8, r9 = p
    
    residuals = np.float64(abs(my_function_ga(x_np, y_np, m1, m2, m3, m4, m5, m6, de1, de2, de3, de4, de5, de6, p1, p2, p3, p4, p5, p6, p7, p8, p9, q1, q2, q3, q4, q5, q6, q7, q8, q9, r1, r2, r3, r4, r5, r6, r7, r8, r9 ) - y_np)).sum()
    #residuals = 0
    return residuals
    #response = my_function_ga(x_np, y_np, m1, m2, m3, m4, m5, m6, de1, de2, de3, de4, de5, de6, p1, p2, p3, p4, p5, p6, p7, p8, p9, q1, q2, q3, q4, q5, q6, q7, q8, q9, r1, r2, r3, r4, r5, r6, r7, r8, r9 )

    #response = 0
    
    #return response




generations = 5
ga = GA(func=ga_fun, n_dim=39, size_pop=2, max_iter=generations, prob_mut=0.001,
        lb=150, ub=420)


best_params, residuals = ga.run()


print('best_x:', best_params, '\n', 'best_y:', residuals)
#print('LEN', len(best_params))
#print('TY', type(best_params))

## THIS IS GONNA BE MY TEST

z_predict_best_params = my_function_ga(x_np, y_np, *best_params)

z_predict_best_params = np.array(z_predict_best_params)
print(DATA)
print("-"*60)
print(z_predict_best_params)

ax_ga.plot_surface(X_REAL, Y_REAL, z_predict_best_params, rstride=1, cstride=1,
                    cmap='winter', edgecolor='none')
""" best_y_generation = ga.generation_best_Y
best_x_generation = ga.generation_best_X


for i in range(1, generations+1):

    # FAKE
    z_prediction_test = my_function_ga(x_np, y_np, *best_x_generation[i - 1])
    #print(z_prediction_test)
    z_prediction_test = np.array(z_prediction_test)
    #print("X", type(z_prediction_test))

    X_REAL_LOOP, Y_REAL_LOOP = np.meshgrid(x, y)
    #print(X_REAL_LOOP)
    #print(z_prediction_test)
    #print("-"*50)
    # ax_ga.plot_wireframe(X_REAL_LOOP, Y_REAL_LOOP, z_prediction_test, color='green')
    ax_ga.plot_surface(X_REAL_LOOP, Y_REAL_LOOP, z_prediction_test, rstride=1, cstride=1,
                    cmap='winter', edgecolor='none')

    #ax_ga.set_xticks(range(len(STATES)))
    #ax_ga.set_xticklabels(STATES)

    #ax_ga.set_yticks(range(len(YEARS)))
    #ax_ga.set_yticklabels(YEARS)


    ax_ga.set_zlabel('Total')
    
    
    #REAL
    #ax.plot_wireframe(X_REAL, Y_REAL, Z_REAL, color='green')
    #ax.plot_surface(X_REAL, Y_REAL, Z_REAL, rstride=1, cstride=1,
    #                cmap='winter', edgecolor='none')

    #ax.set_xticks(range(len(STATES)))
    #ax.set_xticklabels(STATES)

    #ax.set_yticks(range(len(YEARS)))
    #ax.set_yticklabels(YEARS)


    #ax.set_zlabel('Total')

    plt.pause(5)
    ax_ga.cla() """


## FINISH TEST

""" ax_ga.plot_wireframe(X_REAL, Y_REAL, Z_REAL, color='green')
ax_ga.plot_surface(X_REAL, Y_REAL, Z_REAL, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')

ax_ga.set_xticks(range(len(STATES)))
ax_ga.set_xticklabels(STATES)

ax_ga.set_yticks(range(len(YEARS)))
ax_ga.set_yticklabels(YEARS)


ax_ga.set_zlabel('Total') """

#plt.pause(0.01)
# ax_ga.cla()

#plt.ioff()
plt.show()