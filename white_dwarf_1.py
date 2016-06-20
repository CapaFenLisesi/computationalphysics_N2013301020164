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

print c_rou*0.1**3
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
        self.rou=c_rou*self.x**3
        self.pressure=c_p*(self.x*sqrt(1+self.x**2)*(2./3.*self.x**2-1)+arcsinh(self.x))
    def plot_density(self):
        plt.figure()
        self.ax1=plt.subplot(121)
        self.ax2=plt.subplot(122)        
        ax1.plot(self.r,self.rou,'ok',markersize=0.5,label='density')
        ax2.plot(self.r,self.pressure,'ok',markersize=0.5,label='pressure')
        plt.show()
mass=[]
radius=[]
temp_dr=10**-5
x_range=[]
for i in range(-2,3,1):
    for j in linspace(10**i,9.9*10**i,90):
        x_range.append(j)
for i in x_range:
    print 'x=',i,'  dr=',temp_dr
    cmp=LANE_EMDEN(i,temp_dr)
    temp = cmp.calculate()
    mass.append(temp[1])
    radius.append(temp[0])
    temp_dr=cmp.r[-1]*10**-5
mfile=open(r"d:\White_simi.txt",'w')
for j in range(len(mass)):
    print >> mfile, mass[j], radius[j]
mfile.close()
fig=plt.figure(figsize=(8,8))
ax=plt.axes([0.15,0.15,0.7,0.7])
ax.plot(mass,radius,'--ob',markersize=3,label='radius-mass')
ax.set_title('White dwarf : radius versus mass',fontsize=18)
ax.set_xlabel('Mass ( unit= mass of sun )',fontsize=15)
ax.set_ylabel('Radius (unit= radius of sun )',fontsize=15)
plt.show()
