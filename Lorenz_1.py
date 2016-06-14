import math
import matplotlib.pyplot as plt 

sigma=10.0
b=(8.0)/(3.0)
max_time=50
dt=0.0001
N=max_time/dt

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

z_1=lor_gen(5.0)[3]
z_2=lor_gen(10.0)[3]
z_3=lor_gen(25.0)[3]
t=lor_gen(5.0)[0]

line_1,=plt.plot(t,z_1,'r-')
line_2,=plt.plot(t,z_2,'b-')
line_3,=plt.plot(t,z_3,'k-')
plt.xlabel('$t$')
plt.ylabel('$z$')
plt.axis([0,50,0,50])
plt.title('Lorenz Model')
plt.legend([line_1,line_2,line_3],['$r=5$','$r=10$','$r=25$'],fontsize='x-small')
plt.show()
