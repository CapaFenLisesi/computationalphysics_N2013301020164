import matplotlib.pylab as plt
from numpy import *
c_light=3.*(10**8)  
m_e=511.*(10**3)*1.6*(10**-19)/(c_light)**2   # mass of electron
m_b=937.*(10**6)*1.6*(10**-19)/(c_light)**2   # mass of nucleon 
h_bar=6.626*(10**-34)/(2*pi)
lamb=h_bar/(m_e*c_light)              # compton wavelength of electron
niu_e=2.
G_gravity=6.67*(10**-11)
b=c_light*pi/(m_b*niu_e)*sqrt(3.*m_e*lamb**3/G_gravity)    # unit of length
a=(b**3)*m_b*niu_e/(3.*pi**2*lamb**3)                    # unit of mass
m_sun=1.989*10**30
r_sun=6.9599*10**8
c_rou=m_b*niu_e/(3*pi**2*lamb**3)           # unit of density
c_p=3./8.*m_e*c_light**2/(3*pi**2*lamb**3)  # unit of pressure


print 'unit of mass a= %.3f kg'%a
print 'init of length b= %.3f m'%b

class LANE_EMDEN(object):
    def __init__(self, _x0=1, _dr=10**-5, _niu_e=2.):
        self.dr=_dr
        self.r=[self.dr]
        self.m=[0.]
        self.x=[float(_x0)]
        self.niu_e=float(_niu_e)
    def calculate(self):
        while True:
            self.next_m=self.m[-1]+self.dr*4.*pi*self.r[-1]**2*self.x[-1]**3
            self.next_x=self.x[-1]-self.dr*sqrt(1+self.x[-1]**2)/self.x[-1]*self.m[-1]/self.r[-1]**2
            if self.next_x<10**-5 :
                break
            self.r.append(self.r[-1]+self.dr)
            self.m.append(self.next_m)
            self.x.append(self.next_x)
        self.m_star = self.m[-1]*a/m_sun
        self.r_star = self.r[-1]*b/r_sun
        print 'mass = %.3f '%self.m_star,'radius = %.3f'%self.r_star
        return [self.r_star,self.m_star]
    def density(self):
        self.x=array(self.x)
        self.rou=c_rou*self.x**3/10**6
        self.pressure=c_p*(self.x*sqrt(1+self.x**2)*(2./3.*self.x**2-1)+arcsinh(self.x))
        self.radius=b*array(self.r)/r_sun
    def plot_density(self):
        plt.figure()
        self.ax1=plt.subplot(121)
        self.ax2=plt.subplot(122)        
        self.ax1.plot(self.radius,self.rou,'ok',markersize=0.5,label='density')
        self.ax2.plot(self.radius,self.pressure,'ok',markersize=0.5,label='pressure')
        plt.show()

        

cmp=LANE_EMDEN(0.1,10**-5)
cmp.calculate()
cmp.density()

mfile=open(r'd:\white_density.txt','w')
for i in range(len(cmp.radius)):
    print >> mfile, cmp.radius[i], cmp.rou[i]
mfile.close()
cmp.plot_density()
