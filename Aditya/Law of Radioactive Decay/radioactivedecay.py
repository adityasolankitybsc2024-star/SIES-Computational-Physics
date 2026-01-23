import math
import random as rnd
import time
import matplotlib.pyplot as plt

class reaction:
    __kA = 0.7
    __kB = 0.3
    __tfinal = 10
    rnd.seed(time.time())

    def AtoB(self, x1, x2):
        x1 -= 1
        x2 += 1

        x = [x1, x2]
        return x

    def BtoA(self, x1, x2):
        x1 += 1
        x2 -= 1

        x = [x1, x2]
        return x

    def decay(self):
        A = 1000
        B = 0
        t = 0
        Avals = []
        Bvals = []
        tvals = []
        while (t <= self.__tfinal):
            Avals.append(A)
            Bvals.append(B)
            tvals.append(t)

            a1 = self.__kA*A
            a2 = self.__kB*B
            a0 = a1 + a2
            r1 = rnd.uniform(0.0, 1.0)
            r2 = rnd.uniform(0.0, 1.0)

            T = (1/a0)*math.log(1/r1)

            if (r2*a0 <= a1):
                Xval = self.AtoB(A, B)
                A = Xval[0]
                B = Xval[1]
            else:
                Xval = self.BtoA(A, B)
                A = Xval[0]
                B = Xval[1]
                
            t += T
        
        values = [tvals, Avals, Bvals]
        return values
    
    def plot(self):
        values = self.decay()
        plt.title("Plot of reversible reaction consisting of A and B as it reaches equilibrium.", fontdict={'family': 'Arial', 'size':30, 'color':'red'})
        plt.xlabel("time (in seconds)", fontdict={'family': 'Arial', 'size':18, 'color':'black'})
        plt.ylabel("Number of Molecules", fontdict={'family': 'Arial', 'size':18, 'color':'black'})
        plt.grid(True)
        plt.plot(values[0], values[1], color='green', label='Molecules of A')
        plt.plot(values[0], values[2], color='blue', label='Molecules of B')
        plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
        plt.show()

print("This program will plot a graph of a reversible reaction containing 2 molecules A and B as one decays onto another as eventually reaches equilibrium.")
chemical = reaction()
chemical.plot()