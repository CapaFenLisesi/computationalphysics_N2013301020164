import math
import numpy as np
import matplotlib.pyplot as plt 

M=4*((math.pi)**2)
a=0.39
e=0
v0=2*math.pi*(math.sqrt((1-e)/(a*(1+e))))

def path_gen(al):
    x=[a*(1+e)]
    y=[0]
    vx=[0]
    vy=[v0]
    r=[a*(1+e)]
    t=[0]
    loop=0
    dt=0.001
    while loop<1000:
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

mer=path_gen(0.01)
#per=perihelion(mer)
#theta_1=per[1]
#t_1=per[2]
x_1=mer[0]
y_1=mer[1]

mer=path_gen(0.02)
#per=perihelion(mer)
#theta_1=per[1]
#t_1=per[2]
x_2=mer[0]
y_2=mer[1]

mer=path_gen(0.005)
#per=perihelion(mer)
#theta_1=per[1]
#t_1=per[2]
x_3=mer[0]
y_3=mer[1]

mer=path_gen(0.04)
#per=perihelion(mer)
#theta_1=per[1]
#t_1=per[2]
x_4=mer[0]
y_4=mer[1]


plt.figure(1)
plt.subplot(221)
line_1,=plt.plot(x_1,y_1,'r-')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.axis([-0.6,0.6,-0.6,0.6])
plt.title('Mercury\'s Orbit with $\\alpha=0.01$')
plt.legend([line_1],['$\\alpha=0.01$'])

plt.subplot(222)
line_1,=plt.plot(x_2,y_2,'r-')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.axis([-0.6,0.6,-0.6,0.6])
plt.title('Mercury\'s Orbit with $\\alpha=0.02$')
plt.legend([line_1],['$\\alpha=0.02$'])

plt.subplot(223)
line_1,=plt.plot(x_3,y_3,'r-')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.axis([-0.6,0.6,-0.6,0.6])
plt.title('Mercury\'s Orbit with $\\alpha=0.005$')
plt.legend([line_1],['$\\alpha=0.005$'])

plt.subplot(224)
line_1,=plt.plot(x_4,y_4,'r-')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.axis([-0.6,0.6,-0.6,0.6])
plt.title('Mercury\'s Orbit with $\\alpha=0.04$')
plt.legend([line_1],['$\\alpha=0.04$'])


plt.show()
#print [t_1,theta_1]
