import random as rnd
import time

start = time.perf_counter()
rnd.seed(time.time())
N = pow(10, 6)
pnt_sq = 0
pnt_circ = 0
sq_x = []
sq_y = []
circ = []

for i in range(0, N):
    rx = rnd.uniform(-1, 1)
    ry = rnd.uniform(-1, 1)

    d = pow(rx, 2) + pow(ry, 2)
    pnt_sq += 1
    
    if(d <= 1):
        pnt_circ += 1
print("Estimated value of pi using Monte Carlo is", 4*(pnt_circ/pnt_sq))
end = time.perf_counter()

print("Elapsed time : ", end - start)