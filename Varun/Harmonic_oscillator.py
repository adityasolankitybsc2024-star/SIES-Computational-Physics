from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
g = 9.8
r = 0.5
b = 0.5
def f(t, X):
    x, V = X
    return [V, -g/r*np.sin(x) - b*V]
sol = solve_ivp(f,(0,10),[3.14/6,0], t_eval=np.linspace(0,10,400))

theta = []
thetav = []
for angle in sol.y[0]:
    theta.append(angle*(180/3.14))

for anglev in sol.y[1]:
    thetav.append(anglev*(180/3.14))
plt.plot(sol.t,theta, label = 'displacemant')
plt.plot(sol.t,thetav, label = 'velocity')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend(loc = 'upper right')
plt.show()