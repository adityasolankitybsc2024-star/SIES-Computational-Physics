import random as rnd
import matplotlib.pyplot as plt
import time

rnd.seed(time.time())
N = pow(10,5)
distances_x = []
distances_y = []
distances_z = []
x = 0
y = 0
z = 0
P = 1/6

for i in range(0, N):
    R = rnd.uniform(0,1)
    if(R >= 0.0 and R < P):
        x += 1
    elif(R >= P and R < P*2):
        x -= 1
    elif(R >= P*2 and R < P*3):
        y += 1
    elif(R >= P*3 and R < P*4):
        y -= 1
    elif(R >= P*4 and R < P*5):
        z += 1
    elif(R >= P*5 and R < 1):
        z -= 1
    distances_x.append(x)
    distances_y.append(y)
    distances_z.append(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot(distances_x,distances_y,distances_z, color = 'blue')
plt.title('3D Random Walk', color = 'green')
ax.set_xlabel('X-distance', color = 'red')
ax.set_ylabel('Y-distance', color = 'red')
ax.set_zlabel('Z-distance', color = 'red')
plt.show()