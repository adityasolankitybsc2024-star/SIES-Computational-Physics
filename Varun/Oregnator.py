import random as rnd
import matplotlib.pyplot as plt
import math as mt
import time

rnd.seed(time.time())
mol_Y1 = []
mol_Y2 = []
mol_Y3 = []
Val_T = []
sig_1 = 2000
sig_2 = 50000
Y1 = 500
Y2 = 1000
Y3 = 2000
c1X1 = sig_1/Y2
c2 = sig_2/(Y1*Y2)
c3X2 = (sig_1 + sig_2)/Y1
c4 = 2*sig_1/(Y1*Y1)
c5X3 = (sig_1 + sig_2)/Y3
t = 0
while (t<7):
    r1 = rnd.uniform(0, 1)
    r2 = rnd.uniform(0, 1)
        
    a1 = c1X1*Y2
    a2 = c2*Y1*Y2
    a3 = Y1*c3X2
    a4 = ((Y1*(Y1-1))/2)*c4
    a5 = c5X3*Y3

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

plt.plot(Val_T, mol_Y1, label='Y1')
plt.plot(Val_T, mol_Y2, label='Y2')
plt.plot(Val_T, mol_Y3, label='Y3')
plt.xlim(0,7)
plt.ylim(0,9000)
plt.legend(loc = "upper right")
plt.xlabel('Time (s)', color = 'red')
plt.ylabel('Population of molecules', color = 'red')
plt.title('Oregonator Model', color = 'red')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot(mol_Y1, mol_Y2, mol_Y3, color = 'red')
plt.title("Oregonator Model", fontdict={'family':'Times New Roman', 'size':30, 'color':'green'})
ax.set_xlabel("number of Y1 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
ax.set_ylabel("number of Y2 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
ax.set_zlabel("number of Y3 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
plt.show()