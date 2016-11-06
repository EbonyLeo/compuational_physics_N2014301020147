from pylab import * 
import math

g=9.8
q=0.5
l=9.8
f=2.0
omega_D=2.0/3.0
dt=0.04
theta=[]
omega=[]
t=[]
i=1
theta1=[]
omega1=[]

def initialize(_theta, _omega, _t):
    global theta, omega, t
    theta=[]
    omega=[]
    t=[]
    t.append(0.)
    theta.append(0.2)
    omega.append(0.)

def calculate(omega, theta, t,i):
    while t[i-1]<100:
        omega.append(omega[i-1]-(g*theta[i-1]/l+q*omega[i-1]-f*math.sin(omega_D*t[i-1]))*dt)
        theta.append(theta[i-1]+omega[i]*dt)
        if theta[i]>math.pi:
            theta[i]=theta[i]-2*math.pi
        elif theta[i]<-math.pi:
            theta[i]=theta[i]+2*math.pi
        t.append(t[i-1]+dt)
        i=i+1
    return 0

initialize(theta,omega,t)
calculate(omega,theta,t,i)

plot(theta1,omega1,label='Omega versus theta, f_D=2.0')
legend(loc="upper center")
xlabel('Theta (radians) ')
ylabel('Omega (radians/s) ')
xlim(-4,4)
ylim(1.2*min(omega),1.5*max(omega))
show()
    
