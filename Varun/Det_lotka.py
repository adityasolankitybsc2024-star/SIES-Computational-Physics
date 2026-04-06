from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np

C1X = 10
C2 = 0.01
C3 = 10

def f(t, Y):
    Y1,Y2 = Y
    A = C1X*Y1 - C2*Y1*Y2
    B = C2*Y1*Y2 - C3*Y2
    return [A,B]

sol = de(f,(0,5),[500,200],t_eval=np.arange(0,5,0.00001))

plt.plot(sol.t, sol.y[0], label = 'Y1')
plt.plot(sol.t, sol.y[1], label = 'Y2')
plt.title('Deterministic Lotka-Volterra Simulation', color = 'green')
plt.xlabel('Time (t)', color = 'red')
plt.ylabel('Population of Y molecules', color = 'red')
plt.xlim(0,5)
plt.ylim(0,4000)
plt.legend(loc = 'upper right')
plt.grid(True, color = 'gray', linewidth = 0.19)
plt.show()