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

x=lor_gen(25.0)[1]
z=lor_gen(25.0)[3]
t=lor_gen(25.0)[0]

line_1,=plt.plot(x,z,'r,',mew=1.0)
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.axis([-20,20,0,50])
plt.title('Lorenz Model')
plt.legend([line_1],['$r=25$'],fontsize='x-small')
plt.show()
