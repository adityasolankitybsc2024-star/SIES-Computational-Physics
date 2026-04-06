from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math as mt
import time

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


rnd.seed(time.time())

mol_Y1 = []
mol_Y2 = []
mol_Y3 = []
Val_T = []
t = 0

while (t<3):
    r1 = rnd.uniform(0, 1)
    r2 = rnd.uniform(0, 1)
        
    a1 = C1X1*Y2
    a2 = C2*Y1*Y2
    a3 = Y1*C3X2
    a4 = ((Y1*(Y1-1))/2)*C4
    a5 = C5X3*Y3

    a0 = a1 + a2 + a3 + a4 + a5

    dt = (1/a0)*mt.log(1/r1)
    P = r2*a0

    if(P < a1):
        Y1 += 1
        Y2 -= 1
    elif(a1 <= P and P < a1+a2):
        Y2 -= 1
        Y1 -= 1
    elif(a1+a2 <= P and P < a1+a2+a3):
        Y3 += 1
        Y1 += 1
    elif(a1+a2+a3 <= P and P < a1+a2+a3+a4):
        Y1 -= 2
    else:
        Y3 -= 1
        Y2 += 1

    t = t + dt

    mol_Y1.append(Y1)
    mol_Y2.append(Y2)
    mol_Y3.append(Y3)
    Val_T.append(t)   

fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(Val_T, mol_Y1, label='Y1')
axes[0].plot(Val_T, mol_Y2, label='Y2')
axes[0].plot(Val_T, mol_Y3, label='Y3')
axes[0].set_xlim(0,3)
axes[0].set_ylim(0,10000)
axes[0].set_xlabel('Time (s)', color = 'red')
axes[0].set_ylabel('Population of Y molecules', color = 'red')
axes[0].set_title('Stochastic Oregonator Simulation', color = 'red')
axes[0].legend(loc = "upper right")
axes[0].grid(True, color = 'gray', linewidth = 0.19)

axes[1].plot(sol.t, sol.y[0], label = 'Y1')
axes[1].plot(sol.t, sol.y[1], label = 'Y2')
axes[1].plot(sol.t, sol.y[2], label = 'Y3')
axes[1].set_title('Deterministic Oregonator Simulation', color = 'green')
axes[1].set_xlabel('Time (t)', color = 'red')
axes[1].set_ylabel('Population of Y molecules', color = 'red')
axes[1].set_xlim(0,5)
axes[1].set_ylim(0,10000)
axes[1].legend(loc = 'upper right')
axes[1].grid(True, color = 'gray', linewidth = 0.19)
plt.tight_layout()
plt.show()