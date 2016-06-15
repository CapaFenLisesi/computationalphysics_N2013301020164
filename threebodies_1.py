import matplotlib.pylab as plt
from math import *

m_e=6.0*(10**24)
m_j=1.9*(10**27)*200
m_s=2.0*(10**30)
dt=0.0001
t_max=30
step=int(t_max/dt)

ivex=0.0
ivey=2.0*pi
ix_e=1.0
iy_e=0.0

ivjx=0
ivjy=0.977*pi
ix_j=5.2
iy_j=0.0

ivsx=-(m_e*ivex+m_j*ivjx)/m_s
ivsy=-(m_e*ivey+m_j*ivjy)/m_s
ix_s=0
iy_s=0

vex=[]
vey=[]
x_e=[]
y_e=[]

vjx=[]
vjy=[]
x_j=[]
y_j=[]

vsx=[]
vsy=[]
x_s=[]
y_s=[]

def threebody_gen():
    vex.append(ivex)
    vey.append(ivey)
    x_e.append(ix_e)
    y_e.append(iy_e)
    vjx.append(ivjx)
    vjy.append(ivjy)
    x_j.append(ix_j)
    y_j.append(iy_j)
    vsx.append(ivsx)
    vsy.append(ivsy)
    x_s.append(ix_s)
    y_s.append(iy_s)
    for i in range(step):
        rse=((x_s[i]-x_e[i])**2+(y_s[i]-y_e[i])**2)**0.5
        rje=((x_j[i]-x_e[i])**2+(y_j[i]-y_e[i])**2)**0.5
        rsj=((x_s[i]-x_j[i])**2+(y_s[i]-y_j[i])**2)**0.5
        vex.append(vex[i]+(4*(pi**2)*(x_s[i]-x_e[i])/(rse**3)+4*(pi**2)*(m_j/m_s)*(x_j[i]-x_e[i])/(rje**3))*dt)
        vey.append(vey[i]+(4*(pi**2)*(y_s[i]-y_e[i])/(rse**3)+4*(pi**2)*(m_j/m_s)*(y_j[i]-y_e[i])/(rje**3))*dt)
        vjx.append(vjx[i]+(4*(pi**2)*(m_e/m_s)*(x_e[i]-x_j[i])/(rje**3)+4*(pi**2)*(x_s[i]-x_j[i])/(rsj**3))*dt)
        vjy.append(vjy[i]+(4*(pi**2)*(m_e/m_s)*(y_e[i]-y_j[i])/(rje**3)+4*(pi**2)*(y_s[i]-y_j[i])/(rsj**3))*dt)
        vsx.append(vsx[i]+(4*(pi**2)*(m_j/m_s)*(x_j[i]-x_s[i])/(rsj**3)+4*(pi**2)*(m_e/m_s)*(x_e[i]-x_s[i])/(rse**3))*dt)
        vsy.append(vsy[i]+(4*(pi**2)*(m_j/m_s)*(y_j[i]-y_s[i])/(rsj**3)+4*(pi**2)*(m_e/m_s)*(y_e[i]-y_s[i])/(rse**3))*dt)
        x_e.append(x_e[i]+vex[i+1]*dt)
        y_e.append(y_e[i]+vey[i+1]*dt)
        x_j.append(x_j[i]+vjx[i+1]*dt)
        y_j.append(y_j[i]+vjy[i+1]*dt)
        x_s.append(x_s[i]+vsx[i+1]*dt)
        y_s.append(y_s[i]+vsy[i+1]*dt)
        
threebody_gen()


plt.figure(1)
line_1,=plt.plot(x_s,y_s,'r-')
line_2,=plt.plot(x_e,y_e,'b-')
line_3,=plt.plot(x_j,y_j,'k-')
plt.xlabel("X(AU)")
plt.ylabel("Y(AU)")
plt.title('Three Bodies Trajectory')
plt.legend([line_1,line_2,line_3],['Sun','Earth','Jupiter'],fontsize='x-small')
plt.show()
