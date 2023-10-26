#Andres Felipe Garcia Vina
#A01800027

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.67408e-11 # m^3 kg^-1 s^-2
m_earth = 5.972e24 # kg
m_mars = 6.39e23 # kg
m_sun = 1.989e30 # kg
r_earth = 1.496e11 # m
r_mars = 2.279e11 # m

# Initial conditions
x_earth_0 = r_earth # m
y_earth_0 = 0 # m
vx_earth_0 = 0 # m/s
vy_earth_0 = 32670 # m/s  for hoffman transfer orbit 32670 # m/s normal orbit around the sun 29783 # m/s
x_mars_0 = r_mars # m
y_mars_0 = 0 # m
vx_mars_0 = 0 # m/s
vy_mars_0 = 24130 # m/s

# Time
t_0 = 0 # s
t_f = 2*365*24*3600 # s
delta_t = 3600 # s
t = np.arange(t_0, t_f, delta_t)

# Function that returns dx/dt and dy/dt

def model(z,t):
    x_earth = z[0]
    y_earth = z[1]
    vx_earth = z[2]
    vy_earth = z[3]
    x_mars = z[4]
    y_mars = z[5]
    vx_mars = z[6]
    vy_mars = z[7]
    dxdt_earth = vx_earth
    dydt_earth = vy_earth
    dvxdt_earth = -G*m_sun*x_earth/((x_earth**2+y_earth**2)**(3/2))
    dvydt_earth = -G*m_sun*y_earth/((x_earth**2+y_earth**2)**(3/2))
    dxdt_mars = vx_mars
    dydt_mars = vy_mars
    dvxdt_mars = -G*m_sun*x_mars/((x_mars**2+y_mars**2)**(3/2))
    dvydt_mars = -G*m_sun*y_mars/((x_mars**2+y_mars**2)**(3/2))
    return [dxdt_earth, dydt_earth, dvxdt_earth, dvydt_earth, dxdt_mars, dydt_mars, dvxdt_mars, dvydt_mars]

# Initial conditions
z_0 = [x_earth_0, y_earth_0, vx_earth_0, vy_earth_0, x_mars_0, y_mars_0, vx_mars_0, vy_mars_0]

# Solve ODE
z = odeint(model,z_0,t)

# Plot results
plt.figure(1)
if vy_earth_0 == 32670:
    plt.title('Hohmann transfer orbit')
    plt.plot(z[:,0],z[:,1],'b',label='Rocket')

elif vy_earth_0 == 29783:
    plt.title('Normal orbit around the sun')
    plt.plot(z[:,0],z[:,1],'b',label='Earth')
plt.plot(z[:,4],z[:,5],'r',label='Mars')
plt.legend(loc='best')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid()
plt.show()







