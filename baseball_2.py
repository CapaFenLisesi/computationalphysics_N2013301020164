import math
import matplotlib.pyplot as plt   
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
    
def projectile_generator1(omg):
    angle=45
    rad=(angle)*(math.pi)/180     
    v_x=49.1744*(math.cos(rad))
    v_y=49.1744*(math.sin(rad)) 
    v_z=0
    loop=0
    dt=0.01
    g=9.8
    r_x=[0]
    r_y=[0]
    r_z=[0]
    while True:
        if r_y[loop]<-0.0001:
            k=-(r_y[loop-1])/(r_y[loop])
            r_x[loop]=(r_x[loop-1]+k*(r_x[loop]))/(k+1)
            r_y[loop]=(0)
            break 
        else:
            temp_x=r_x[-1]
            temp_y=r_y[-1]
            temp_z=r_z[-1]
            temp_v=math.sqrt((v_x)**2+(v_y)**2+(v_z)**2)
            temp_b=0.0039+(0.0058)/(1+math.exp((temp_v-35)/5))
            temp_s=0.00041
            temp_vx=v_x
            r_x.append(r_x[loop]+v_x*dt)
            r_y.append(r_y[loop]+v_y*dt)
            r_z.append(r_z[loop]+v_z*dt)
            v_x=v_x-(v_x*(temp_v)*temp_b)*dt
            v_y=v_y-(g+temp_b*temp_v*v_y)*dt
            v_z=v_z-temp_s*omg*v_x*dt
            loop=loop+1
    return [r_x,r_y,r_z]

def projectile_generator2(angle):
    rad=(angle)*(math.pi)/180     
    v_x=700*(math.cos(rad))
    v_y=700*(math.sin(rad)) 
    loop=0
    dt=0.01
    g=9.8
    r_x=[0]
    r_y=[0]
    while True:
        if r_y[loop]<-0.0001:
            k=-(r_y[loop-1])/(r_y[loop])
            r_x.append((r_x[loop-1]+k*(r_x[loop]))/(k+1))
            r_y.append(0)
            break 
        else:
            r_x.append(r_x[loop]+v_x*dt)
            r_y.append(r_y[loop]+v_y*dt)
            temp_v=math.sqrt((v_x)**2+(v_y)**2)
            v_x=v_x-v_x*(temp_v)*0.00004*dt
            v_y=v_y-v_y*(temp_v)*0.00004*dt-g*dt
            loop=loop+1
    return [r_x,r_y]

def find():
    omg=-200
    temp=projectile_generator1(omg)
    max_x=temp[0][-1]
    max_omg=omg
    while omg<400:
        temp_1=projectile_generator1(omg+1)
        temp_x=temp_1[0][-1]
        if max_x<temp_x:
            max_x=temp_x
            max_omg=omg+1
        omg=omg+1
    return max_omg

a=projectile_generator1(200)
x_1=a[0]
y_1=a[1]
z_1=a[2]
b=projectile_generator1(0)
x_2=b[0]
y_2=b[1]
z_2=b[2]
c=projectile_generator1(30)
x_3=c[0]
y_3=c[1]
z_3=c[2]
d=projectile_generator1(-30)
x_4=d[0]
y_4=d[1]
z_4=d[2]
e=projectile_generator1(100)
x_5=e[0]
y_5=e[1]
z_5=e[2]

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('z (m)', fontsize=18)
ax.set_ylabel('x (m)', fontsize=18)
ax.set_zlabel('y (m)', fontsize=18)
ax.plot(x_1,z_1,y_1,   label='$\\omega=200rps$')
ax.plot(x_2,z_2,y_2,   label='no spin')
ax.plot(x_3,z_3,y_3,   label='$\\omega=30rps$')
ax.plot(x_4,z_4,y_4,   label='$\\omega=-30rps$')
ax.plot(x_5,z_5,y_5,   label='$\\omega=100rps$')
ax.legend()
plt.show()
