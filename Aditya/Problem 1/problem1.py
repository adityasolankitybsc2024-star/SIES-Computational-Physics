import random as rnd
import time 
import math
import matplotlib.pyplot as plt

class Reactions:
    __tfinal = 10
    __Y1vals = []
    __Y2vals = []
    __Tvals = []
    __c1X1 = 5000
    __c2X2 = 50
    __c3 = 0.00005
    __c4 = 5
    rnd.seed(time.time())

    def reaction1(self, Y1):
        Y1 += 1
        return Y1
    
    def reaction2(self, Y1, Y2):
        Y1 -= 1
        Y2 += 1
        vals = [Y1, Y2]
        return vals
    
    def reaction3(self, Y1, Y2):
        Y1 += 1
        Y2 -= 1
        vals = [Y1, Y2]
        return vals
    
    def reaction4(self, Y1):
        Y1 -= 1
        return Y1

    def a(self, Y1, Y2):
        a1 = self.__c1X1
        a2 = self.__c2X2*Y1
        a3 = self.__c3*(Y1*(Y1 - 1)/2)*Y2
        a4 = self.__c4*Y1
        a0 = a1 + a2 + a3 + a4
        vals = [a0, a1, a2, a3, a4]
        return vals

    def process(self):
            Y1 = 1000
            Y2 = 2000
            t = 0
            while (t <= self.__tfinal):
                self.__Y1vals.append(Y1)
                self.__Y2vals.append(Y2)
                self.__Tvals.append(t)
                r1 = rnd.uniform(0, 1)
                r2 = rnd.uniform(0, 1)
                p = self.a(Y1, Y2)
                dt = (1/p[0])*math.log(1/r1)

                if (0 <= r2*p[0] and r2*p[0] < p[1]):
                    Y1 = self.reaction1(Y1)
                elif (p[1] <= r2*p[0] and r2*p[0] < (p[1] + p[2])):
                    Y = self.reaction2(Y1, Y2)
                    Y1 = Y[0]
                    Y2 = Y[1]
                elif ((p[1] + p[2]) <= r2*p[0] and r2*p[0] < (p[1] + p[2] + p[3])):
                    Y = self.reaction3(Y1, Y2)
                    Y1 = Y[0]
                    Y2 = Y[1]
                else:
                    Y1 = self.reaction4(Y1)
                
                t += dt

    def plot(self):
        plt.figure(1)
        plt.title("Gillespie paper Fig 14 for Y1", fontdict={'family':'Times New Roman', 'size':30, 'color':'red'})
        plt.xlabel("time (s)", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        plt.ylabel("number of Y1 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        # plt.grid(True, color='gray', linewidth=1)
        plt.plot(self.__Tvals, self.__Y1vals)

        plt.figure(2)
        plt.title("Gillespie paper Fig 14 for Y2", fontdict={'family':'Times New Roman', 'size':30, 'color':'red'})
        plt.xlabel("time (s)", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        plt.ylabel("number of Y2 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        # plt.grid(True, color='gray', linewidth=1)
        plt.plot(self.__Tvals, self.__Y2vals)

        plt.figure(3)
        plt.title("Gillespie paper Fig 14 attractor", fontdict={'family':'Times New Roman', 'size':30, 'color':'red'})
        plt.xlabel("number of Y1 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        plt.ylabel("number of Y2 molecules", fontdict={'family':'Times New Roman', 'size':18, 'color':'red'})
        # plt.grid(True, color='gray', linewidth=1)
        plt.plot(self.__Y1vals, self.__Y2vals)

        plt.show()

print("This Program will plot the graphs of the Gillespie Research paper.")
KMC = Reactions()
KMC.process()
KMC.plot()