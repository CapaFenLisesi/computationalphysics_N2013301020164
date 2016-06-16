import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from math import *



max_loop=1000
def initial():
    v=[[0 for i in range(31)] for j in range(31)]
    for n_1 in range(31):
        for n_2 in range(31):
            v[n_1][n_2]=0.0

    for n_1 in range(10,21):
        v[n_1][10]=-1.0
        v[n_1][20]=1.0
    for n_1 in range(31):
        v[n_1][0]=0.0
        v[n_1][30]=0.0
        v[0][n_1]=0.0
        v[30][n_1]=0.0
    return v

v=initial()


v2=[]
n=0

for itotal in range(max_loop):
    v2=None
    v2=[[0 for i in range(31)] for j in range(31)]

    vbegin=None
    vbegin=[[0 for i in range(31)] for j in range(31)]
    for n_1 in range(31):
        for n_2 in range(31):
            vbegin[n_1][n_2]=v[n_1][n_2]
            v2[n_1][n_2]=v[n_1][n_2]

    for n_1 in range(1,len(v)-1):
        for n_2 in range(1,len(v[0])-1):
            v2[n_1][n_2]=(v[n_1-1][n_2]+v[n_1+1][n_2]+v[n_1][n_2-1]+v[n_1][n_2+1])/4.0

    for n_3 in range(10,21):
        v2[n_3][10]=-1.0
        v2[n_3][20]=1.0

    delta_v=None
    delta_v=[]
    for n_1 in range(31):
        for n_2 in range(31):
            abs(vbegin[n_1][n_2]-v2[n_1][n_2])

    v=None
    v=[[0 for i in range(31)] for j in range(31)]
    for n_1 in range(31):
        for n_2 in range(31):
            v[n_1][n_2]=v2[n_1][n_2]

    ntotal=itotal

strn=str(ntotal)
print strn

X=[]
Y=[]

for i in range(31):
    X.append(-3.0+6*i/30.0)
    Y.append(-3.0+6*i/30.0)

CS = plt.contour(X, Y, v, 20,colors='red')
plt.clabel(CS, fontsize=9, inline=1)
plt.title("Electric Potential Distribution with 1000 Iterations")
plt.xlabel("x")
plt.ylabel("y")
plt.plot([-1,-1],[-1,1],color = "black",linewidth=3)
plt.plot([1,1],[1,-1],color = "brown",linewidth=3)
plt.plot([3,-3,-3,3,3],[3,3,-3,-3,3],color = "yellow",linewidth=3)
plt.show()
