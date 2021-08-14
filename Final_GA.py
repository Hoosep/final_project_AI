import numpy as np, random, operator, pandas as pd, sys, matplotlib.pyplot as plt, matplotlib.cm as cm, math, time
from mpl_toolkits import mplot3d

from mpl_toolkits.mplot3d import Axes3D
X = []
Y = []
Z = []

def CreateGraph():
    m1=0
    m2=.6
    m3=1.2
    m4=0
    m5=.6
    m6=1.2
    de1=0.5
    de2=0.5
    de3=0.5
    de4=0.5
    de5=0.5
    de6=0.5
    p1=0
    p2=0
    p3=0
    p4=10
    p5=10
    p6=10
    p7=0
    p8=0
    p9=0
    q1=0
    q2=0
    q3=0
    q4=10
    q5=10
    q6=10
    q7=0
    q8=0
    q9=0
    r1=0
    r2=0
    r3=0
    r4=0
    r5=0
    r6=0
    r7=0
    r8=0
    r9=0

    for i in range(1,10):
        for j in range(1,10):
            x=i/10
            y=j/10
            mf1=math.exp((-(x-m1)**2)/(2*de1**2))
            mf2=math.exp((-(x-m2)**2)/(2*de2**2))
            mf3=math.exp((-(x-m3)**2)/(2*de3**2))
            mf4=math.exp((-(y-m4)**2)/(2*de4**2))
            mf5=math.exp((-(y-m5)**2)/(2*de5**2))
            mf6=math.exp((-(y-m6)**2)/(2*de6**2))
            inf1=mf1*mf4
            inf2=mf1*mf5
            inf3=mf1*mf6
            inf4=mf2*mf4
            inf5=mf2*mf5
            inf6=mf2*mf6
            inf7=mf3*mf4
            inf8=mf3*mf5
            inf9=mf3*mf6
            reg1=inf1*(p1*x+q1*y+r1)
            reg2=inf2*(p2*x+q2*y+r2)
            reg3=inf1*(p3*x+q3*y+r3)
            reg4=inf1*(p4*x+q4*y+r4)
            reg5=inf1*(p5*x+q5*y+r5)
            reg6=inf1*(p6*x+q6*y+r6)
            reg7=inf1*(p7*x+q7*y+r7)
            reg8=inf1*(p8*x+q8*y+r8)
            reg9=inf1*(p9*x+q9*y+r9)
            b=inf1+inf2+inf3+inf4+inf5+inf6+inf7+inf8+inf9
            a=reg1+reg2+reg3+reg4+reg5+reg6+reg7+reg8+reg9
            z=a/b
            X.append(x)
            Y.append(y)
            Z.append(z)
    print(X)
    XGraph, YGraph, ZGraph = np.array(X), np.array(Y), np.array(Z)
    print(X)
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_trisurf(X, Y, Z, linewidth=0, antialiased=False)
    ax.set_title('Surface plot')
    plt.show()

def main():
    CreateGraph()
if __name__=="__main__":
    main()