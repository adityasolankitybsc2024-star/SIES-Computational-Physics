from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np

Y1 = 500
Y2 = 1000
Y3 = 2000
sig_1 = 2000
sig_2 = 50000
C1X1 = sig_1/Y2
C2 = sig_2/(Y1*Y2)
C3X2 = (sig_1 + sig_2)/Y1
C4 = 2*sig_1/(Y1*Y1)
C5X3 = (sig_1 + sig_2)/Y3

def f(t, Y):
    Y1,Y2,Y3 = Y
    A = C1X1*Y2 - C2*Y1*Y2 + C3X2*Y1 - C4*Y1*Y1
    B = - C1X1 - C2*Y1*Y2 + C5X3*Y3
    C = C3X2*Y1 - C5X3*Y3
    return [A,B,C]

sol = de(f,(0,5),[Y1,Y2,Y3],t_eval=np.arange(0,5,0.000001))

plt.plot(sol.t, sol.y[0], label = 'Y1')
plt.plot(sol.t, sol.y[1], label = 'Y2')
plt.plot(sol.t, sol.y[2], label = 'Y3')
plt.title('Deterministic Oregonator Simulation', color = 'green')
plt.xlabel('Time (t)', color = 'red')
plt.ylabel('Population of Y molecules', color = 'red')
plt.xlim(0,5)
plt.ylim(0,10000)
plt.legend(loc = 'upper right')
plt.grid(True, color = 'gray', linewidth = 0.19)
plt.show()