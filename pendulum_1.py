import math
import matplotlib.pyplot as plt 

theta=[0]
t=[0]
w=[0.1]
omg=9.8
dt=0.0001
t_max=20
N=(t_max)/(dt)
q=1.0

def pendulum_gen(omg_d):
    loop=0
    shit=[0.2]
    fuck=[-0.1]
    pee=[0]
    while loop<N:
        f=0.2*(math.sin(omg_d*pee[loop]))        
        fuck.append(fuck[loop]-(omg*shit[loop]+q*fuck[loop]-f)*dt)
        shit.append(shit[loop]+fuck[-1]*dt)
        pee.append(pee[loop]+dt)
        loop=loop+1
    return [shit,fuck,pee]


a_ttl=pendulum_gen(2.0)
b_ttl=pendulum_gen(3.13)
c_ttl=pendulum_gen(4.0)

theta_u=a_ttl[0]
theta_c=b_ttl[0]
theta_o=c_ttl[0]
t_e=a_ttl[2]

line_1,=plt.plot(t_e,theta_u,'r-')
line_2,=plt.plot(t_e,theta_c,'k-')
line_3,=plt.plot(t_e,theta_o,'b-')
plt.xlabel('t(s)')
plt.ylabel('$\\theta$')
plt.axis([0,20,-0.2,0.2])
plt.title('Driven Pendulum with Different Forced Frequencies')
plt.legend([line_1,line_2,line_3],['$\\omega_D=2.0$','$\\omega_D=3.13$','$\\omega_D=4.0$'],fontsize='x-small')
plt.show()

