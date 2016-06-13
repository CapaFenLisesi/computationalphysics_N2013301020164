import math
import matplotlib.pyplot as plt   
    
def projectile_generator1(omg):
    angle=45
    rad=(angle)*(math.pi)/180     
    v_x=49.1744*(math.cos(rad))
    v_y=49.1744*(math.sin(rad)) 
    v_z=0
    loop=0
    dt=0.01
    g=9.8
    temp=[]
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
            v_x=v_x-(v_x*(temp_v)*temp_b+temp_s*omg*v_y)*dt
            v_y=v_y-(g+temp_b*temp_v*v_y-temp_s*omg*v_x)*dt
            v_z=v_z
            temp.append(temp_v)
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


r_x1=projectile_generator1(-30)[0]
r_y1=projectile_generator1(-30)[1]
r_x2=projectile_generator1(30)[0]
r_y2=projectile_generator1(30)[1]
r_x3=projectile_generator1(100)[0]
r_y3=projectile_generator1(100)[1]
r_x4=projectile_generator1(200)[0]
r_y4=projectile_generator1(200)[1]
r_x5=projectile_generator1(700)[0]
r_y5=projectile_generator1(700)[1]
r_x6=projectile_generator1(1000)[0]
r_y6=projectile_generator1(1000)[1]
r_x7=projectile_generator1(1500)[0]
r_y7=projectile_generator1(1500)[1]

line_1,=plt.plot(r_x1,r_y1,'r-')
line_2,=plt.plot(r_x2,r_y2,'m-')
line_3,=plt.plot(r_x3,r_y3,'b-')
line_4,=plt.plot(r_x4,r_y4,'g-')
line_5,=plt.plot(r_x5,r_y5,'k-')
line_6,=plt.plot(r_x6,r_y6,'c-')
line_7,=plt.plot(r_x7,r_y7,'y-')

plt.ylabel('y')
plt.xlabel('x')
plt.title('Numerical Solution of Baseball Motion(2-d case)')
plt.legend([line_1,line_2,line_3,line_4,line_5,line_6,line_7],['$\\omega=-30rps$','$\\omega=30rps$','$\\omega=100rps$','$\\omega=200rps$','$\\omega=700rps$','$\\omega=1000rps$','$\\omega=1500rps$'],fontsize='x-small')
plt.show()
