import math
import numpy as np
import matplotlib.pyplot as plt 

M=4*((math.pi)**2)
a=0.39
e=0.206

def path_gen(al):
    x=[a*(1+e)]
    y=[0]
    vx=[0]
    vy=[8.2]
    r=[a*(1+e)]
    t=[0]
    loop=0
    dt=0.001
    while loop<2500:
        vx.append(vx[-1]-((M*x[-1]*dt)/((r[-1])**3))*(1+(al/(r[-1])**2)))
        vy.append(vy[-1]-((M*y[-1]*dt)/((r[-1])**3))*(1+(al/(r[-1])**2)))
        x.append(x[-1]+(vx[-1])*dt)
        y.append(y[-1]+(vy[-1])*dt)
        r.append(math.sqrt((x[-1])**2+(y[-1])**2))
        t.append(t[-1]+dt)        
        loop=loop+1
    return [x,y,r,t]

def perihelion(M):
    x=M[0]
    y=M[1]
    r=M[2]
    t=M[3]
    r_p=[]
    theta_p=[]
    t_p=[]
    loop=1
    count=len(r)
    while loop<count-1:
        if (r[loop+1]-r[loop])*(r[loop]-r[loop-1])<0:
            if r[loop]<a:
                if y[loop]>0:                   
                    temp_th=(np.arccos(x[loop]/r[loop]))*(180)/(math.pi)
                elif y[loop]<0:
                    temp_th=(-np.arccos(x[loop]/r[loop])+2*(math.pi))*(180)/(math.pi)
                theta_p.append(temp_th)
                t_p.append(t[loop])
                r_p.append(r[loop])
        loop=loop+1
    return [r_p,theta_p,t_p]

mer=path_gen(0)
per=perihelion(mer)
#theta_1=per[1]
#t_1=per[2]
a_1=[0.0008,0.001,0.002,0.0035,0.0005,0]
d_1=[8.044,10.2,21.57,38.65,5.114,-0.1642]
d_2=[]
for fuck in a_1:
    shit=fuck*(1.12*((10)**4))-0.5877
    d_2.append(shit)
#x=mer[0]
#y=mer[1]

plt.figure(1)
line_1,=plt.plot(a_1,d_1,'ro')
line_2,=plt.plot(a_1,d_2,'k-')
plt.xlabel('$\\alpha$')
plt.ylabel('$d\\theta/dt$(degrees/Yr)')
plt.title('Simulation of the Precession of Mercury')
plt.axis([0,0.004,0,40])
plt.legend([line_2],['Precession Rate versus $\\alpha$'])
plt.show()
#print [t_1,theta_1]
