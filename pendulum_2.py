import math
import matplotlib.pyplot as plt 
import numpy as np

omg_d=3.13
f=0.2
q=np.linspace(0,3,1000)
theta_0=(f)/(omg_d*q)


line_1,=plt.plot([0.5,1.0,1.5,2.0],[0.128,0.064,0.043,0.032],'ro')
line_2,=plt.plot(q,theta_0,'k-')
plt.xlabel('t(s)')
plt.ylabel('$\\theta$')
plt.axis([0,3,0,1])
plt.title('Amplitude-Friction Diagram')
plt.annotate('$\\theta_0=\\frac{F_D}{\Omega_Dq}$',xy=(0.25,0.256),xytext=(1,0.3),arrowprops=dict(facecolor='black', shrink=0.05),fontsize=25)
plt.legend([line_1,line_2],['Numerical Results','Theoretical Curve'])
plt.show()

