import math
import matplotlib.pyplot as plt 

omg=1
dt=0.04
t_max=4000
N=(t_max)/(dt)
N_i=int(N)
q=0.5
omg_d=(2.0)/(3.0)
period=3*math.pi
N_p=int(period/dt)

def pendulum_gen():
    loop=0
    shit=[0.2]
    fuck=[0]
    pee=[0]
    while loop<N:
        f=(1.2)*(math.sin(omg_d*pee[loop]))        
        fuck.append(fuck[loop]-(omg*(math.sin(shit[loop]))+q*fuck[loop]-f)*dt)
        if (shit[loop]+fuck[-1]*dt)>math.pi:
            temp_1=shit[loop]+fuck[-1]*dt-2*math.pi
            shit.append(temp_1)
        elif (shit[loop]+fuck[-1]*dt)<-math.pi:
            temp_2=shit[loop]+fuck[-1]*dt+2*math.pi
            shit.append(temp_2)
        else:
            shit.append(shit[loop]+fuck[-1]*dt)
        pee.append(pee[loop]+dt)
        loop=loop+1
    return [shit,fuck,pee]


theta_o=pendulum_gen()[0]
w_o=pendulum_gen()[1]
t_e=pendulum_gen()[2]

theta_1=[]
w_1=[]
i=0
while i<N:
    for n in range(8000):
        if abs(t_e[i]-(3*n*math.pi))<0.5*dt:
            theta_1.append(theta_o[i])
            w_1.append(w_o[i])
    i=i+1 
   
theta_2=[]
w_2=[]
j=0
while j<N:
    for n in range(8000):
        if abs(t_e[j]-((2*n+0.5)*(math.pi)/(omg_d)))<0.5*dt:
            theta_2.append(theta_o[j])
            w_2.append(w_o[j])
    j=j+1 

theta_3=[]
w_3=[]
s=0
while s<N:
    for n in range(8000):
        if abs(t_e[s]-((2*n+0.25)*(math.pi)/(omg_d)))<0.5*dt:
            theta_3.append(theta_o[s])
            w_3.append(w_o[s])
    s=s+1 

plt.figure(1)
plt.subplot(131)
line_1,=plt.plot(theta_1,w_1,'ro')
plt.xlabel('$\\theta$')
plt.ylabel('$\\omega$')
plt.title('Phase Trajectory')
plt.legend([line_1],['$F_D=1.2$'],fontsize='x-small')

plt.subplot(132)
line_1,=plt.plot(theta_2,w_2,'ro')
plt.xlabel('$\\theta$')
plt.ylabel('$\\omega$')
plt.legend([line_1],['$F_D=1.2$'],fontsize='x-small')

plt.subplot(133)
line_1,=plt.plot(theta_3,w_3,'ro')
plt.xlabel('$\\theta$')
plt.ylabel('$\\omega$')
plt.legend([line_1],['$F_D=1.2$'],fontsize='x-small')

plt.show()
