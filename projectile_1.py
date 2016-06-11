import math
import matplotlib.pyplot as plt   

    
def projectile_generator(angle):
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
            v_x=v_x*(1-0.00004*dt)
            v_y=v_y*(1-0.00004*dt)-g*dt
            loop=loop+1
    return [r_x,r_y]
def find():
    angle=35
    temp=projectile_generator(angle)
    max_x=temp[0][-1]
    max_theta=angle
    while angle<45:
        temp_1=projectile_generator(angle+1)
        temp_x=temp_1[0][-1]
        if max_x<temp_x:
            max_x=temp_x
            max_theta=angle+1
        angle=angle+1
    return max_theta

a=find()
r_x1=projectile_generator(35)[0]
r_y1=projectile_generator(35)[1]
r_x2=projectile_generator(40)[0]
r_y2=projectile_generator(40)[1]
r_x3=projectile_generator(45)[0]
r_y3=projectile_generator(45)[1]
r_x4=projectile_generator(50)[0]
r_y4=projectile_generator(50)[1]
r_x5=projectile_generator(55)[0]
r_y5=projectile_generator(55)[1]

line_5,=plt.plot(r_x5,r_y5,'b-')
line_1,=plt.plot(r_x1,r_y1,'r-')
line_2,=plt.plot(r_x2,r_y2,'k-')
line_3,=plt.plot(r_x3,r_y3,'g-')
line_4,=plt.plot(r_x4,r_y4,'y-')
plt.axis([0,60000,0,20000])
plt.ylabel('y')
plt.xlabel('x')
plt.title('Numerical Solution of Projectile Motion(Air Drag-Free)')
plt.legend([line_1,line_2,line_3,line_4,line_5],['$\\theta=35^\circ$','$\\theta=40^\circ$','$\\theta=45^\circ$','$\\theta=50^\circ$','$\\theta=55^\circ$'],fontsize='x-small')
plt.show()

