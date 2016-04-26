import matplotlib.pyplot as plt
from math import e

N_1=[5]
N_2=[5]
N_3=[5]
N_4=[5]
t_1=[0]
t_2=[0]
t_3=[0]
t_4=[0]
dt_1=0.0005
dt_2=0.0005
dt_3=0.0005
dt_4=0.0005
t_max=0.5
step_1=int(t_max/dt_1)
step_2=int(t_max/dt_2)
step_3=int(t_max/dt_3)
step_4=int(t_max/dt_4)

#Following codes perform numerical calculation.
loop_1=0
while loop_1<step_1:
    temp_11=(1+10*dt_1)*(N_1[loop_1])-3*(dt_1)*((N_1[loop_1])**2)
    temp_1t=t_1[loop_1]+dt_1
    N_1.append(temp_11)
    t_1.append(temp_1t)
    loop_1=loop_1+1



loop_2=0
while loop_2<step_2:
    temp_21=(1+10*dt_2)*(N_2[loop_2])-2*(dt_2)*((N_2[loop_2])**2)
    temp_2t=t_2[loop_2]+dt_2
    N_2.append(temp_21)
    t_2.append(temp_2t)
    loop_2=loop_2+1

loop_3=0
while loop_3<step_3:
    temp_31=(1+10*dt_3)*(N_3[loop_3])-1*(dt_3)*((N_3[loop_3])**2)
    temp_3t=t_3[loop_3]+dt_3
    N_3.append(temp_31)
    t_3.append(temp_3t)
    loop_3=loop_3+1

loop_4=0
while loop_4<step_4:
    temp_41=(1+10*dt_4)*(N_4[loop_4])-0.5*(dt_4)*((N_4[loop_4])**2)
    temp_4t=t_4[loop_4]+dt_4
    N_4.append(temp_41)
    t_4.append(temp_4t)
    loop_4=loop_4+1


#The following codes plot the data.
plt.figure(1)
plt.subplot(211)
line_1,=plt.plot(t_1,N_1,'r-')
line_2,=plt.plot(t_2,N_2,'k-')
line_3,=plt.plot(t_3,N_3,'g-')
line_4,=plt.plot(t_4,N_4,'y-')
plt.axis([0,0.5,0,10])
plt.ylabel('Population')
plt.title('Numerical Solution of Population Growth')
plt.legend([line_1,line_2,line_3,line_4],['$b=3$','$b=2$','$b=1$','$b=0.5$'],fontsize='x-small')

plt.subplot(212)
line_1,=plt.plot(t_1,N_1,'r-')
line_2,=plt.plot(t_2,N_2,'k-')
line_3,=plt.plot(t_3,N_3,'g-')
line_4,=plt.plot(t_4,N_4,'y-')
plt.axis([0,0.5,0,20])
plt.ylabel('Population')
plt.xlabel('Time')
plt.title('Numerical Solution of Population Growth')
plt.legend([line_1,line_2,line_3,line_4],['$b=3$','$b=2$','$b=1$','$b=0.5$'],fontsize='x-small')
plt.show()



