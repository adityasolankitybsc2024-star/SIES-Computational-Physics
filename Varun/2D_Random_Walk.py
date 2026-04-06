import random as rnd
import matplotlib.pyplot as plt
import time

rnd.seed(time.time())
N = 1000
distances_x = []
distances_y = []
x = 0
y = 0

for i in range(0, N):
    R = rnd.uniform(0,1)
    if(R >= 0.0 and R < 0.25):
        x += 1
    elif(R >= 0.25 and R < 0.5):
        x -= 1
    elif(R >= 0.5 and R < 0.75):
        y += 1
    elif(R >= 0.75 and R < 1.0):
        y -= 1
    distances_x.append(x)
    distances_y.append(y)
plt.plot(distances_x, distances_y)
plt.show()