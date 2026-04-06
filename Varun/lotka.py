import random as rnd
import matplotlib.pyplot as plt
import math as mt
import time

rnd.seed(time.time())
mol_Y1 = []
mol_Y2 = []
Val_T = []
c1X = 10
c2 = 0.01
c3 = 10
Y1 = 1000
Y2 = 1000
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

plt.plot(Val_T, mol_Y1)
# plt.plot(mol_Y1, mol_Y2)
plt.xlabel('Population of Y1 molecules', color = 'red')
plt.ylabel('Population of Y2 molecules', color = 'red')
# plt.xlim(0,5000)
# plt.ylim(0,5000)
plt.title('Lotka Model', color = 'red')
plt.show()