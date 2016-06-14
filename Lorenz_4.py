import math
import matplotlib.pyplot as plt 

sigma=10.0
b=(8.0)/(3.0)
max_time=50
dt=0.0001
N=max_time/dt
N_i=int(N)

def lor_gen(r):
    x=[1]
    y=[0]
    z=[0]
    t=[0]
    loop=0
    while loop<N:
        x.append((sigma*(y[loop]-x[loop]))*dt+x[loop])
        y.append((-(x[loop])*(z[loop])+r*(x[loop])-y[loop])*dt+y[loop])
        z.append(((x[loop])*(y[loop])-b*(z[loop]))*dt+z[loop])
        t.append(t[loop]+dt)
        loop=loop+1
    return [t,x,y,z]

z_1=lor_gen(160.0)[3]
t_1=lor_gen(160.0)[0]
z_2=lor_gen(163.8)[3]
t_2=lor_gen(163.8)[0]

loop_1=0
while loop_1<N:
    z_2[loop_1]=z_2[loop_1]+200
    loop_1=loop_1+1


plt.figure(1)
line_1,=plt.plot(t_1,z_1,'r-')
line_2,=plt.plot(t_1,z_2,'k-')
plt.xlabel('t')
plt.ylabel('z')
plt.axis([0,30,0,600])
plt.title('Lorenz model, z versus time')
plt.legend([line_1,line_2],['$r=160.0$','$r=163.8$'],fontsize='x-small')
plt.show()

