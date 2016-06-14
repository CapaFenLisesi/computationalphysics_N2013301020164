import math
import matplotlib.pyplot as plt 

sigma=10.0
b=(8.0)/(3.0)
max_time=500
dt=0.0001
N=max_time/dt
N_i=int(N)

def lor_gen(r,x_0,y_0,z_0):
    x=[x_0]
    y=[y_0]
    z=[z_0]
    t=[0]
    loop=0
    while loop<N:
        x.append((sigma*(y[loop]-x[loop]))*dt+x[loop])
        y.append((-(x[loop])*(z[loop])+r*(x[loop])-y[loop])*dt+y[loop])
        z.append(((x[loop])*(y[loop])-b*(z[loop]))*dt+z[loop])
        t.append(t[loop]+dt)
        loop=loop+1
    return [t,x,y,z]

x_o=lor_gen(25.0,1.0,0.0,0.0)[1]
y_o=lor_gen(25.0,1.0,0.0,0.0)[2]
z_o=lor_gen(25.0,1.0,0.0,0.0)[3]
t_o=lor_gen(25.0,1.0,0.0,0.0)[0]

x=[]
y=[]
z=[]
for i in range(N_i):
    if x_o[i]>0.0 and x_o[i+1]<0.0:
        y.append(y_o[i])
        z.append(z_o[i])
    if x_o[i]<0.0 and x_o[i+1]>0.0:
        y.append(y_o[i])
        z.append(z_o[i])

x_1=[]
y_1=[]
z_1=[]
for i in range(N_i):
    if y_o[i]>0.0 and y_o[i+1]<0.0:
        x_1.append(x_o[i])
        z_1.append(z_o[i])
    if y_o[i]<0.0 and y_o[i+1]>0.0:
        x_1.append(x_o[i])
        z_1.append(z_o[i])

'''
x_i=lor_gen(25.0,0.0,1.0,0.0)[1]
y_i=lor_gen(25.0,0.0,1.0,0.0)[2]
z_i=lor_gen(25.0,0.0,1.0,0.0)[3]
t_i=lor_gen(25.0,0.0,1.0,0.0)[0]

x_2=[]
y_2=[]
z_2=[]
for i in range(N_i):
    if x_i[i]>0.0 and x_i[i+1]<0.0:
        y_2.append(y_i[i])
        z_2.append(z_i[i])
    if x_i[i]<0.0 and x_i[i+1]>0.0:
        y_2.append(y_i[i])
        z_2.append(z_i[i])

x_3=[]
y_3=[]
z_3=[]
for i in range(N_i):
    if y_i[i]>0.0 and y_i[i+1]<0.0:
        x_3.append(x_i[i])
        z_3.append(z_i[i])
    if y_i[i]<0.0 and y_i[i+1]>0.0:
        x_3.append(x_i[i])
        z_3.append(z_i[i])
'''
plt.figure(1)
plt.subplot(121)
plt.scatter(y,z,s=1)
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-10,10,0,30])
plt.title('IC:$x_0=1,y_0=0,z_0=0$')

plt.subplot(122)
plt.scatter(x_1,z_1,s=1)
plt.xlabel('x')
plt.ylabel('z')
plt.axis([-20,20,0,40])
plt.title('IC:$x_0=1,y_0=0,z_0=0$')
'''
plt.subplot(223)
plt.scatter(y_2,z_2,s=1)
plt.xlabel('y')
plt.ylabel('z')
plt.axis([-10,10,0,30])
plt.title('IC:$x_0=0,y_0=1,z_0=0$')

plt.subplot(224)
plt.scatter(x_3,z_3,s=1)
plt.xlabel('x')
plt.ylabel('z')
plt.axis([-20,20,0,40])
plt.title('IC:$x_0=0,y_0=1,z_0=0$')
'''
plt.show()

