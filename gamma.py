#Import the matplotlib module.
import matplotlib.pyplot as plt
from math import e

def calculate(local):
    value=20*(e**(-local))-10
    return value

def calculate_x(local):
    value=-20*(e**(-local))-10*local+20
    return value

#Define some of the variables in the program. For convenience, these variables have been initialized.
v_1=[10]
v_2=[10]
v_3=[10]
v_4=[10]
v_5=[10]
x_1=[0]
x_2=[0]
x_3=[0]
x_4=[0]
x_5=[0]
t_1=[0]
t_2=[0]
t_3=[0]
t_4=[0]
t_5=[0]
g=10
mu_1=0
mu_2=0.5
mu_3=1
mu_4=2
mu_5=4
dt=0.05
t_max=7
step=int(t_max/dt)

#Following codes perform numerical calculation.
loop_1=0
while loop_1<step:
    temp_11=v_1[loop_1]-g*dt-mu_1*v_1[loop_1]*(dt)
    temp_12=x_1[loop_1]+((v_1[loop_1]+temp_11)*(dt))/2
    temp_1t=t_1[loop_1]+dt
    v_1.append(temp_11)
    x_1.append(temp_12)
    t_1.append(temp_1t)
    loop_1=loop_1+1

loop_2=0
while loop_2<step:
    temp_21=v_2[loop_2]-g*dt-mu_2*v_2[loop_2]*(dt)
    temp_22=x_2[loop_2]+((v_2[loop_2]+temp_21)*(dt))/2
    temp_2t=t_2[loop_2]+dt
    v_2.append(temp_21)
    x_2.append(temp_22)
    t_2.append(temp_2t)
    loop_2=loop_2+1

loop_3=0
while loop_3<step:
    temp_31=v_3[loop_3]-g*dt-mu_3*v_3[loop_3]*(dt)
    temp_32=x_3[loop_3]+((v_3[loop_3]+temp_31)*(dt))/2
    temp_3t=t_3[loop_3]+dt
    v_3.append(temp_31)
    x_3.append(temp_32)
    t_3.append(temp_3t)
    loop_3=loop_3+1

loop_4=0
while loop_4<step:
    temp_41=v_4[loop_4]-g*dt-mu_4*v_4[loop_4]*(dt)
    temp_42=x_4[loop_4]+((v_4[loop_4]+temp_41)*(dt))/2
    temp_4t=t_4[loop_4]+dt
    v_4.append(temp_41)
    x_4.append(temp_42)
    t_4.append(temp_4t)
    loop_4=loop_4+1

loop_5=0
while loop_5<step:
    temp_51=v_5[loop_5]-g*dt-mu_5*v_5[loop_5]*(dt)
    temp_52=x_5[loop_5]+((v_5[loop_5]+temp_51)*(dt))/2
    temp_5t=t_5[loop_5]+dt
    v_5.append(temp_51)
    x_5.append(temp_52)
    t_5.append(temp_5t)
    loop_5=loop_5+1


#The following codes plot the data.
plt.figure(1)

plt.subplot(211)
line_1,=plt.plot(t_1,v_1,'r-')
line_2,=plt.plot(t_2,v_2,'k-')
line_3,=plt.plot(t_3,v_3,'g-')
line_4,=plt.plot(t_4,v_4,'y-')
line_5,=plt.plot(t_5,v_5,'b-')
plt.axis([0,7,-20,10])
plt.ylabel('Velocity(m/s)')
plt.title('Numerical Solution of Velocity')
plt.legend([line_1,line_2,line_3,line_4,line_5],['$\\gamma=0$','$\\gamma=0.5kg/s$','$\\gamma=1kg/s$','$\\gamma=2kg/s$','$\\gamma=4kg/s$'],fontsize='x-small')

plt.subplot(212)
line_1,=plt.plot(t_1,x_1,'r-')
line_2,=plt.plot(t_2,x_2,'k-')
line_3,=plt.plot(t_3,x_3,'g-')
line_4,=plt.plot(t_4,x_4,'y-')
line_5,=plt.plot(t_5,x_5,'b-')
plt.axis([0,7,-20,10])
plt.ylabel('Displacement(m)')
plt.xlabel('Time(s)')
plt.title('Numerical Solution of Displacement')
plt.legend([line_1,line_2,line_3,line_4,line_5],['$\\gamma=0$','$\\gamma=0.5kg/s$','$\\gamma=1kg/s$','$\\gamma=2kg/s$','$\\gamma=4kg/s$'],fontsize='x-small')


plt.show()

