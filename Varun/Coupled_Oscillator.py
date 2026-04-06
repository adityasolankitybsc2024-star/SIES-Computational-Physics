# Varun Vinayak Phatak
# FMPHY2526260
# MSc Part-1
# Core Lab Practical - Coupled Oscillator

from scipy.integrate import solve_ivp as de
import matplotlib.pyplot as plt
import numpy as np 

m1,m2,m3 = 1,2,1
k1,k2 = 1,1.5
X0 = [0,0.4,0.2,0,0,0]
def f(t, Y):
    x1,x2,x3, v1,v2,v3 = Y
    dv1dt = -(k1/m1)*x1 + (k1/m1)*x2
    dv2dt =  (k1/m2)*x1 - ((k1+k2)/m2)*x2 + (k2/m2)*x3
    dv3dt = (k2/m3)*x2 - (k2/m3)*x3
    return[v1,v2,v3,dv1dt,dv2dt,dv3dt]

sol = de(f, (0,40), X0, t_eval=np.arange(0,40,0.01))

plt.plot(sol.t,sol.y[0], color = 'red', label = 'M1')
plt.plot(sol.t,sol.y[1], color = 'blue', label = 'M2')
plt.plot(sol.t,sol.y[2], color = 'green', label = 'M3')
plt.xlabel('Time (t)', color = 'red')
plt.ylabel('Position', color = 'red')
plt.title('Coupled Oscillator', color = 'green')
plt.legend(loc = 'upper right')
plt.show()


a11 = k1/m1
a12 = -k1/m1
a13 = 0
a21 = -k1/m2
a22 = ((k1+k2)/m2)
a23 = -k2/m2
a31 = 0 
a32 = -k2/m3
a33 = k2/m3

A = np.array([[a11,a12,a13],
              [a21,a22,a23],
              [a31,a32,a33]])
eigen_val,eigen_vec = np.linalg.eig(A)

print('Eigen value', eigen_val)
print('Eigen vector', eigen_vec)

f = np.sqrt(eigen_val)
print('Frequency : ',f)

X0 = np.array ([0 , 0.4 ,0.2])
R = eigen_vec
C = np.linalg.inv (R) @ X0

print ('Amplitude of each normal mode:', C)