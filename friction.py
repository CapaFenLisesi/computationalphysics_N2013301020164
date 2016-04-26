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
v_th=[10]
x_1=[0]
x_2=[0]
x_3=[0]
x_4=[0]
x_5=[0]
x_th=[0]
t_1=[0]
t_2=[0]
t_3=[0]
t_4=[0]
t_5=[0]
t_th=[0]
g=10
mu=1
dt_1=0.9
dt_2=0.5
dt_3=0.4
dt_4=0.1
dt_5=0.05
t_max=7
step_1=int(t_max/dt_1)
step_2=int(t_max/dt_2)
step_3=int(t_max/dt_3)
step_4=int(t_max/dt_4)
step_5=int(t_max/dt_5)

#Following codes perform numerical calculation.
loop_1=0
while loop_1<step_1:
    temp_11=v_1[loop_1]-g*dt_1-mu*v_1[loop_1]*(dt_1)
    temp_12=x_1[loop_1]+((v_1[loop_1]+temp_11)*(dt_1))/2
    temp_1t=t_1[loop_1]+dt_1
    v_1.append(temp_11)
    x_1.append(temp_12)
    t_1.append(temp_1t)
    loop_1=loop_1+1

loop_2=0
while loop_2<step_2:
    temp_21=v_2[loop_2]-g*dt_2-mu*v_2[loop_2]*(dt_2)
    temp_22=x_2[loop_2]+((v_2[loop_2]+temp_21)*(dt_2))/2
    temp_2t=t_2[loop_2]+dt_2
    v_2.append(temp_21)
    x_2.append(temp_22)
    t_2.append(temp_2t)
    loop_2=loop_2+1

loop_3=0
while loop_3<step_3:
    temp_31=v_3[loop_3]-g*dt_3-mu*v_3[loop_3]*(dt_3)
    temp_32=x_3[loop_3]+((v_3[loop_3]+temp_31)*(dt_3))/2
    temp_3t=t_3[loop_3]+dt_3
    v_3.append(temp_31)
    x_3.append(temp_32)
    t_3.append(temp_3t)
    loop_3=loop_3+1

loop_4=0
while loop_4<step_4:
    temp_41=v_4[loop_4]-g*dt_4-mu*v_4[loop_4]*(dt_4)
    temp_42=x_4[loop_4]+((v_4[loop_4]+temp_41)*(dt_4))/2
    temp_4t=t_4[loop_4]+dt_4
    v_4.append(temp_41)
    x_4.append(temp_42)
    t_4.append(temp_4t)
    loop_4=loop_4+1

loop=0
while loop<step_5:
    temp_1=t_th[loop]+dt_5
    temp_2=calculate(temp_1)
    temp_3=calculate_x(temp_1)
    t_th.append(temp_1)
    v_th.append(temp_2)
    x_th.append(temp_3)
    loop=loop+1


#The following codes plot the data.
plt.figure(1)

plt.subplot(121)
line_th,=plt.plot(t_th,v_th,'b-')
line_1,=plt.plot(t_1,v_1,'ro')
line_2,=plt.plot(t_2,v_2,'ko')
line_3,=plt.plot(t_3,v_3,'go')
line_4,=plt.plot(t_4,v_4,'yo')
plt.axis([0,7,-12,10])
plt.ylabel('Velocity(m/s)')
plt.xlabel('Time(s)')
plt.title('Numerical Solution of Velocity')
plt.legend([line_th,line_1,line_2,line_3,line_4],['Theoretical Curve','$\\tau=0.9s$','$\\tau=0.5s$','$\\tau=0.4s$','$\\tau=0.1s$'],fontsize='x-small')

plt.subplot(122)
linex_th,=plt.plot(t_th,x_th,'b-')
linex_1,=plt.plot(t_1,x_1,'ro')
linex_2,=plt.plot(t_2,x_2,'ko')
linex_3,=plt.plot(t_3,x_3,'go')
linex_4,=plt.plot(t_4,x_4,'yo')
plt.axis([0,6,-20,10])
plt.ylabel('Displacement(m)')
plt.xlabel('Time(s)')
plt.title('Numerical Solution of Displacement')
plt.legend([linex_th,linex_1,linex_2,linex_3,linex_4],['Theoretical Curve','$\\tau=0.9s$','$\\tau=0.5s$','$\\tau=0.4s$','$\\tau=0.1s$'],fontsize='x-small')

plt.show()




