import math
import matplotlib.pyplot as plt   

    
def projectile_generator1(angle):
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
            temp_x=r_x[-1]
            temp_y=r_y[-1]
            temp_f=(1-((0.0065*temp_y)/288))**(2.5)
            r_x.append(r_x[loop]+v_x*dt)
            r_y.append(r_y[loop]+v_y*dt)
            temp_v=math.sqrt((v_x)**2+(v_y)**2)
            v_x=v_x-v_x*(temp_v)*0.00004*dt*temp_f
            v_y=v_y-v_y*(temp_v)*0.00004*dt*temp_f-g*dt
            loop=loop+1
    return [r_x,r_y]

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
    angle=35
    temp=projectile_generator1(angle)
    max_x=temp[0][-1]
    max_theta=angle
    while angle<55:
        temp_1=projectile_generator1(angle+0.1)
        temp_x=temp_1[0][-1]
        if max_x<temp_x:
            max_x=temp_x
            max_theta=angle+0.1
        angle=angle+0.1
    return max_theta

a=find()

r_x1=projectile_generator1(43.8)[0]
r_y1=projectile_generator1(43.8)[1]
r_x2=projectile_generator2(43.8)[0]
r_y2=projectile_generator2(43.8)[1]
r_x3=projectile_generator1(35)[0]
r_y3=projectile_generator1(35)[1]
r_x4=projectile_generator2(35)[0]
r_y4=projectile_generator2(35)[1]

line_1,=plt.plot(r_x1,r_y1,'r-')
line_2,=plt.plot(r_x2,r_y2,'r--')
line_3,=plt.plot(r_x3,r_y3,'b-')
line_4,=plt.plot(r_x4,r_y4,'b--')
plt.axis([0,25000,0,10000])
plt.ylabel('y')
plt.xlabel('x')
plt.title('Numerical Solution of Projectile Motion(Air Drag)')
plt.legend([line_1,line_2,line_3,line_4],['$\\theta=43.8^\circ$(With Density Correction)','$\\theta=43.8^\circ$Without Density Correction','$\\theta=35.0^\circ$(With Density Correction)','$\\theta=35.0^\circ$Without Density Correction'],fontsize='x-small')
plt.show()

