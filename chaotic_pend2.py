import math
import matplotlib.pyplot as plt 

omg=1
dt=0.04
t_max=400
N=(t_max)/(dt)
N_i=int(N)
q=0.5
omg_d=(2.0)/(3.0)
period=3*math.pi
N_p=int(period/dt)

def pendulum_gen(f_d):
    loop=0
    shit=[0.2]
    fuck=[0]
    pee=[0]
    while loop<N:
        f=(f_d)*(math.sin(omg_d*pee[loop]))        
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

def pendulum_gen1(f_d):
    loop=0
    shit=[0.199]
    fuck=[0]
    pee=[0]
    while loop<N:
        f=(f_d)*(math.sin(omg_d*pee[loop]))        
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


a_ttl=pendulum_gen(0.5)[0]
b_ttl=pendulum_gen(0.5)[1]
c_ttl=pendulum_gen(1.2)[0]
d_ttl=pendulum_gen(1.2)[1]


t_e=a_ttl[2]

#theta_p=[]
#w_p=[]
#i=0
#while i<N:
#    for n in range(8000):
#        if abs(t_e[i]-(3*n*math.pi))<0.5*dt:
#            theta_p.append(theta_u[i])
#            w_p.append(w_u[i])
#    i=i+1    

plt.figure(1)
plt.subplot(211)
line_1,=plt.plot(a_ttl,b_ttl,'r-')
plt.xlabel('$\\theta$')
plt.ylabel('$\\omega$')
plt.title('Phase Trajectory')
plt.legend([line_1],['$F_D=0.5$'],fontsize='x-small')

plt.subplot(212)
line_1,=plt.plot(c_ttl,d_ttl,'r+')
plt.xlabel('$\\theta$')
plt.ylabel('$\\omega$')
plt.legend([line_1],['$F_D=1.2$'],fontsize='x-small')

plt.show()
