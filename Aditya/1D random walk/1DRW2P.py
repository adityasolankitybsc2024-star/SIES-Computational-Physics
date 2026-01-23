import random as rnd
import time
import matplotlib.pyplot as plt

class lattice:
    rnd.seed(time.time())
    __N = pow(10, 6)
    __lowlim = -10
    __uplim = 10

    def action(self, pos1, pos2):
        r1 = rnd.uniform(0.0, 1.0)
        r2 = rnd.uniform(0.0, 1.0)
        if (r1 >= 0 and r1 < 0.5):
            pos1 -= 1
        else:
            pos1 += 1

        if (r2 >= 0 and r2 < 0.5):
            pos2 -= 1
        else:
            pos2 += 1

        pos = [pos1, pos2]
        return pos
    
    def iteration(self):
        flag = False
        x1 = 0
        x2 = 8
        count = 0
        Time = []
        positions1 = []
        positions2 = []
        for i in range(0, self.__N):
            positions1.append(x1)
            positions2.append(x2)
            Time.append(count)
            if (flag == True):
                break
            pos = self.action(x1, x2)
            if (pos[0] < self.__lowlim):
                x1 = 10
                x2 = pos[1]
            elif (pos[0] > self.__uplim):
                x1 = -10
                x2 = pos[1]
            elif (pos[1] < self.__lowlim):
                x1 = pos[0]
                x2 = 10
            elif (pos[1] > self.__uplim):
                x1 = pos[0]
                x2 = -10
            else:
                x1 = pos[0]
                x2 = pos[1]
            count += 1
            if (x1 == x2):
                flag = True

        values = [positions1, positions2, Time]
        return values

    def plot(self):
        values = self.iteration()
        meet_point = values[0][-1]
        meet_time = values[2][-1]
        print(f"The point at which the 2 random walkers, which are seperated by a distance of 8 meters, meet is {meet_point} meters from the position of 1st walker and at time {meet_time} seconds")
        plt.title("Plot of position of two random walkers in 1D lattice", fontdict={'family':'Times New Roman', 'color':'red', 'size':30})
        plt.xlabel("time in seconds", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.ylabel("position of random walkers in meters", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        plt.plot(values[2], values[0], color='green', linewidth=2.0, label="position of x1")
        plt.plot(values[2], values[1], color='violet', linewidth=2.0, label="position of x2")
        plt.legend(loc="lower left")
        plt.show()

    def multiple(self):
        sumt = 0
        sump = 0
        for j in range(0, 1000):
            values = self.iteration()
            sumt += values[2][-1]
            sump += values[0][-1]
        
        mean_position = sump/1000
        mean_time = sumt/1000
        mean_values = [mean_position, mean_time]
        return mean_values
        
    def historgam(self):
        times = []
        positions = []
        for k in range(0, 1000):
            values = self.iteration()
            times.append(values[2][-1])
            positions.append(values[0][-1])
        
        plt.title("Distribution curve of position", fontdict={'family':'Times New Roman', 'color':'red', 'size':30})
        plt.xlabel("distances of the 2 walkers at multiple iterations", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.ylabel("frequency of the 2 walkers meeting at a distance range", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        plt.hist(positions, bins=100, color='green', edgecolor="black")
        plt.show()

        plt.title("Distribution curve of time", fontdict={'family':'Times New Roman', 'color':'red', 'size':30})
        plt.xlabel("times taken by 2 walkers to meet over multiple iterations", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.ylabel("frequency of the 2 walkers meeting at a particular time range", fontdict={'family':'Times New Roman', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        plt.hist(times, bins=100, color='green', edgecolor='black')
        plt.show()

print("This program will show the plot of position vs time for 2 1D random walkers  and where they intersect")
version = lattice()
version.plot()
values = version.multiple()
version.historgam()
print(f"The mean time for the meeting of the 2 random walkers seperated by a distance of 8 meters is {values[1]} seconds and the mean position is {values[0]} meters from the start position of 1st random walker.")
