import random as rnd
import matplotlib.pyplot as plt
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
    # print(Val_T[-1])

# plt.plot(Val_T, mol_Y1)
plt.plot(mol_Y1, mol_Y2)
plt.xlabel('Population of Y1 molecules', color = 'red')
plt.ylabel('Population of Y2 molecules', color = 'red')
plt.title('Brusselator Model', color = 'red')
plt.show()