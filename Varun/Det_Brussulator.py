from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math as mt
import time

rnd.seed(time.time())
mol_Y1 = []
mol_Y2 = []
Val_T = []
c1X1 = 5000
c2X2 = 50
c3 = 0.00005
c4 = 5
Y1 = 1000
Y2 = 2000
t = 0
while (t<10):
    r1 = rnd.uniform(0, 1)
    r2 = rnd.uniform(0, 1)
        
    a1 = c1X1
    a2 = c2X2*Y1
    a3 = ((Y1*(Y1-1))/2)*Y2*c3
    a4 = c4*Y1

    a0 = a1 + a2 + a3 + a4

    dt = (1/a0)*mt.log(1/r1)
    P = r2*a0

    if(P < a1):
        Y1 += 1
    elif(a1 <= P and P < a1+a2):
        Y2 += 1
        Y1 -= 1
    elif(a1+a2 <= P and P < a1+a2+a3):
        Y2 -= 1
        Y1 += 1
    else:
        Y1 -= 1

    t = t + dt

    mol_Y1.append(Y1)
    mol_Y2.append(Y2)
    Val_T.append(t)   

C1X1 = 5000
C2X2 = 50
C3 = 0.00005
C4 = 5

def f(t, Y):
    Y1,Y2 = Y
    A = C1X1 - C2X2*Y1 + (C3/2)*Y1*Y1*Y2 - C4*Y1
    B = C2X2*Y1 - (C3/2)*Y1*Y1*Y2
    return [A,B]

sol = de(f,(0,10),[900,1200],t_eval=np.arange(0,10,0.00001))

fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(Val_T, mol_Y1, label = 'Y1')
axes[0].plot(Val_T, mol_Y2, label = 'Y2')
axes[0].set_xlabel('Time (t)', color = 'red')
axes[0].set_ylabel('Population of Y molecules', color = 'red')
axes[0].set_title('Stochastic Brusselator Simulation', color = 'red')
axes[0].set_xlim(0,10)
axes[0].set_ylim(0,9000)
axes[0].legend(loc = 'upper right')
axes[0].grid(True, color = 'gray', linewidth = 0.19)

axes[1].plot(sol.t, sol.y[0], label = 'Y1')
axes[1].plot(sol.t, sol.y[1], label = 'Y2')
axes[1].set_title('Deterministic Brusselator Simulation', color = 'green')
axes[1].set_xlabel('Time (t)', color = 'red')
axes[1].set_ylabel('Population of Y molecules', color = 'red')
axes[1].set_xlim(0,10)
axes[1].set_ylim(0,9000)
axes[1].legend(loc = 'upper right')
axes[1].grid(True, color = 'gray', linewidth = 0.19)

plt.tight_layout()
plt.show()