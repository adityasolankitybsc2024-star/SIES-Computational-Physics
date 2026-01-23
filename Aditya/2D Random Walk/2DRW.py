import random as rnd
import time
import matplotlib.pyplot as plt

class lattice:
    rnd.seed(time.time())
    __N = 1000

    def action(self, xpos, ypos):
        r = rnd.uniform(0.0, 1.0)
        if (r >= 0 and r < 0.25):
            xpos -= 1
        elif (r >= 0.25 and r < 0.5):
            xpos += 1
        elif (r >= 0.5 and r < 0.75):
            ypos -= 1
        else:
            ypos += 1

        pos = [xpos, ypos]
        return pos
    
    def iteration(self):
        xvalues = []
        yvalues = []
        x = 0
        y = 0
        for i in range(0, self.__N):
            xvalues.append(x)
            yvalues.append(y)
            value = self.action(x, y)
            x = value[0]
            y = value[1]
        
        values = [xvalues, yvalues]
        return values
    
    def single(self):
        values = self.iteration()
        plt.title("Plot of the path taken by a 2D random walker", fontdict={'family':'Arial', 'color':'red', 'size':30})
        plt.xlabel("xposition in meters", fontdict={'family':'Arial', 'color':'black', 'size':18})
        plt.ylabel("yposition in meters", fontdict={'family':'Arial', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        plt.plot(values[0], values[1], color='brown', linewidth=2)
        plt.show()
    
    def positions(self):
        positions = []
        for j in range(0, 1000):
            values = self.iteration()
            positions.append(values)

        return positions
    
    def multiple(self):
        positions = self.positions()
        plt.title("Plot of the path taken by a 2D random walker over multiple iterations", fontdict={'family':'Arial', 'color':'red', 'size':30})
        plt.xlabel("xpositions in meters", fontdict={'family':'Arial', 'color':'black', 'size':18})
        plt.ylabel("ypositions in meters", fontdict={'family':'Arial', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        for k in range(0, len(positions)):
            plt.plot(positions[k][0], positions[k][1], linewidth=2) 
        plt.show()
        
    def calculations(self):
        positions = self.positions()
        sum = 0
        sqsum = 0
        for k in range(0, len(positions)):
            sum += pow((pow(positions[k][0][-1], 2)+pow(positions[k][1][-1], 2)), 0.5)
            sqsum += pow(pow((pow(positions[k][0][-1], 2)+pow(positions[k][1][-1], 2)), 0.5), 2)

        fmoment = sum/len(positions)        
        smoment = sqsum/len(positions)
        moments = [fmoment, smoment]
        return moments

print("This Program will print the paths of 2D Random walker over single and multiple iterations.")
version = lattice()
version.single()
version.multiple()
moment = version.calculations()
print(f"The end to end distance mean is {moment[0]:.4f} meters and end to end distance second moment is {moment[1]:.4f} meters.")
