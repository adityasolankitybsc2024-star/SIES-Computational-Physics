import random as rnd
import time

class EstimatePi:
    rnd.seed(time.time())
    __N = pow(10, 7)
    
    def areacheck(self):
        circle = 0
        square = 0
        
        for i in range(0, self.__N):
            x = rnd.uniform(-1.0, 1.0)
            y = rnd.uniform(-1.0, 1.0)
            if (pow(x, 2) + pow(y, 2) <= 1):
                circle += 1
            else:
                square += 1
        
        pi = 4*(circle/self.__N)

        return pi

print(f"This program estimates the value of pi using Monte carlo method.")
perform = EstimatePi()
pi = perform.areacheck()
print(f"The value of pi estimated is {pi:.10f}")

