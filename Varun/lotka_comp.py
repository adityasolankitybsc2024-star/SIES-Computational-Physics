from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math as mt
import time

C1X = 10
C2 = 0.01
C3 = 10

def f(t, Y):
    Y1,Y2 = Y
    A = C1X*Y1 - C2*Y1*Y2
    B = C2*Y1*Y2 - C3*Y2
    return [A,B]

sol = de(f,(0,5),[500,200],t_eval=np.arange(0,5,0.00001))



rnd.seed(time.time())
mol_Y1 = []
mol_Y2 = []
Val_T = []
c1X = 10
c2 = 0.01
c3 = 10
Y1 = 500
Y2 = 200
t = 0
while (t<10):
    r1 = rnd.uniform(0, 1)
    r2 = rnd.uniform(0, 1)
        
    a1 = Y1*c1X
    a2 = Y1*Y2*c2
    a3 = Y2*c3

    a0 = a1 + a2 + a3
    dt = (1/a0)*mt.log(1/r1)
    P = r2*a0

    if(P < a1):
        Y1 += 1
    elif(a1 <= P and P < a1+a2):
        Y2 += 1
        Y1 -= 1
    else:
        Y2 -= 1
    t = t + dt
    mol_Y1.append(Y1)
    mol_Y2.append(Y2)
    Val_T.append(t)   

fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(Val_T, mol_Y1, label = 'Y1')
axes[0].plot(Val_T, mol_Y2, label = 'Y2')
axes[0].set_xlabel('Time (t)', color = 'red')
axes[0].set_ylabel('Population of Y molecules', color = 'red')
axes[0].set_title('Stochastic Lotka-Volterra Simulation', color = 'red')
axes[0].set_xlim(0,5)
axes[0].set_ylim(0,4000)
axes[0].legend(loc = 'upper right')
axes[0].grid(True, color = 'gray', linewidth = 0.19)

axes[1].plot(sol.t, sol.y[0], label = 'Y1')
axes[1].plot(sol.t, sol.y[1], label = 'Y2')
axes[1].set_title('Deterministic Lotka-Volterra Simulation', color = 'green')
axes[1].set_xlabel('Time (t)', color = 'red')
axes[1].set_ylabel('Population of Y molecules', color = 'red')
axes[1].set_xlim(0,5)
axes[1].set_ylim(0,4000)
axes[1].legend(loc = 'upper right')
axes[1].grid(True, color = 'gray', linewidth = 0.19)
plt.tight_layout()
plt.show()