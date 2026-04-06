from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np

C1X = 5
C2 = 0.005
Y = [[3000],[10]]
Sol = []

def f(t, Y):
    return C1X*Y[0] - C2*Y[0]*Y[0]

for y in Y:
    sol = de(f,(0,5),y, method = 'RK45',t_eval=np.arange(0,5,0.00001))
    Sol.append(sol)


plt.plot(Sol[0].t, Sol[0].y[0], label = '3000')
plt.plot(Sol[1].t, Sol[1].y[0], label = '10')
plt.title('Deterministic Two Reaction Model Simulation', color = 'green')
plt.xlabel('Time (t)', color = 'red')
plt.ylabel('Population of Y molecules', color = 'red')
plt.xlim(0,5)
plt.ylim(0,4000)
plt.legend(loc = 'upper right')
plt.grid(True, color = 'gray', linewidth = 0.19)
plt.show()