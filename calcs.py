import math
G = 6.67408e-11
M = 1.989e30
#1) earth velocity
#distance between the sun and the earth
r1 = 1.496e11
vearth = math.sqrt(G*M/r1)
print(f'Velocity of the earth: {vearth} m/s')
#2) mars velocity
#distance between the sun and mars
r2 = 2.279e11
vmars = math.sqrt(G*M/r2)
print(f'Velocity of mars: {vmars} m/s')
#3) semimajor axis
a = (r1+r2)/2
print(f'Semimajor axis: {a} m')
#4) calculus for mars transfer
#4.1) Dv_departure
Dv_departure = math.sqrt(G*M*((2/r1)-(1/a)))-vearth
print(f'Dv_departure: {Dv_departure} m/s')
#4.2) Dv_arrival
Dv_arrival = vmars - math.sqrt(G*M*((2/r2)-(1/a)))
print(f'Dv_arrival: {Dv_arrival} m/s')
#4) velocity of departure and arrival
v_departure = vearth + Dv_departure
v_arrival = vmars - Dv_arrival
print(f'Velocity of departure: {v_departure} m/s')
print(f'Velocity of arrival: {v_arrival} m/s')
#5) time of flight
t_transfer = math.pi*math.sqrt((a**3)/(G*M))
print(f'Time of flight: {t_transfer} s')
#in days
t_transfer_days = t_transfer/(60*60*24)
print(f'Time of flight: {t_transfer_days} days')