#Import the matplotlib module.
import matplotlib.pyplot as plt
from math import e

def calculate(local):
    value=70*e**(local)
    return value

N_th=[70]
N_1=[70]
N_2=[70]
N_3=[70]
N_4=[70]
t_1=[0]
t_2=[0]
t_3=[0]
t_4=[0]
t_th=[0]
dt_1=0.9
dt_2=0.4
dt_3=0.2
dt_4=0.05
dt_th=0.05
t_max=7
step_1=int(t_max/dt_1)
step_2=int(t_max/dt_2)
step_3=int(t_max/dt_3)
step_4=int(t_max/dt_4)
step_th=int(t_max/dt_th)

#Following codes perform numerical calculation.
loop_1=0
while loop_1<step_1:
    temp_11=(1+dt_1)*(N_1[loop_1])
    temp_1t=t_1[loop_1]+dt_1
    N_1.append(temp_11)
    t_1.append(temp_1t)
    loop_1=loop_1+1

loop_2=0
while loop_2<step_2:
    temp_21=(1+dt_2)*(N_2[loop_2])
    temp_2t=t_2[loop_2]+dt_2
    N_2.append(temp_21)
    t_2.append(temp_2t)
    loop_2=loop_2+1

loop_3=0
while loop_3<step_3:
    temp_31=(1+dt_3)*(N_3[loop_3])
    temp_3t=t_3[loop_3]+dt_3
    N_3.append(temp_31)
    t_3.append(temp_3t)
    loop_3=loop_3+1

loop_4=0
while loop_4<step_4:
    temp_41=(1+dt_4)*(N_4[loop_4])
    temp_4t=t_4[loop_4]+dt_4
    N_4.append(temp_41)
    t_4.append(temp_4t)
    loop_4=loop_4+1

loop_th=0
while loop_th<step_th:
    temp_t=t_th[loop_th]+dt_th
    temp_th=calculate(temp_t)
    N_th.append(temp_th)
    t_th.append(temp_t)
    loop_th=loop_th+1

#The following codes plot the data.

line_th,=plt.plot(t_th,N_th,'b-')
line_1,=plt.plot(t_1,N_1,'ro')
line_2,=plt.plot(t_2,N_2,'ko')
line_3,=plt.plot(t_3,N_3,'go')
line_4,=plt.plot(t_4,N_4,'yo')
plt.axis([0,7,0,80000])
plt.ylabel('Population')
plt.xlabel('Time')
plt.title('Numerical Solution of Population Growth')
plt.legend([line_th,line_1,line_2,line_3,line_4],['Theoretical Curve','$\\tau=0.9$','$\\tau=0.4$','$\\tau=0.2$','$\\tau=0.05$'],fontsize='x-small')
plt.show()

