import random as rnd
import time
import math
import matplotlib.pyplot as plt

start = time.perf_counter()

class reactions:
    __tfinal = 100
    __c1 = 0.1
    __c2 = 2
    __X_bar = 500
    rnd.seed(time.time())
    __Xmol = []
    __Ymol = []
    __Zmol = []
    __tval = []

    def reaction1(self, Y):
        Y += 1
        return Y

    def reaction2(self, Y, Z):
        Y -= 2
        Z += 1
        mol = [Y, Z]
        return mol

    def a(self, Y):
        a1 = self.__c1*self.__X_bar*Y
        a2 = self.__c2*(Y*(Y - 1))/2
        a0 = a1 + a2
        propensities = [a1, a2, a0]
        return propensities
    
    def process(self):
        t = 0
        Y = 10
        Z = 0
        while(t <= self.__tfinal):
            self.__Xmol.append(self.__X_bar)
            self.__Ymol.append(Y)
            self.__Zmol.append(Z)
            self.__tval.append(t)
            r1 = rnd.uniform(0.0, 1.0)
            r2 = rnd.uniform(0.0, 1.0)

            propensities = self.a(Y)

            if (propensities[2] <= 0):
                break
        
            else:
                T = (1/propensities[2])*math.log(1/r1)

            if (r2*propensities[2] <= propensities[0]):
                Y = self.reaction1(Y)

            else:
                molecules = self.reaction2(Y, Z)
                Y = molecules[0]
                Z = molecules[1]

            t += T

    def plot(self):
        plt.title("Plot of system of 2 reactions and number of its molecules over time.", fontdict={'family':'Times New Roman', 'size':30, 'color':'red'})
        plt.xlabel("time (in seconds)", fontdict={'family':'Times New Roman', 'size':18, 'color':'black'})
        plt.ylabel("number of mulecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'black'})
        plt.grid(True, linewidth=2, color="gray")
        plt.plot(self.__tval, self.__Xmol, linewidth=2, color='violet', label="Molecules of Xbar")
        plt.plot(self.__tval, self.__Ymol, linewidth=2, color='green', label="Molecules of Y")
        plt.plot(self.__tval, self.__Zmol, linewidth=2, color='blue', label="Molecules of Z")
        plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
        plt.show()

print("This Program will plot a graph of system having 2 reactions and the number of molecules as they change for reactants.")
chemical = reactions()
chemical.process()
chemical.plot()

end = time.perf_counter()
print(f"The code took {(end - start):.6f} seconds to run.")