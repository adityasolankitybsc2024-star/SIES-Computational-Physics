import random as rnd
import time
import matplotlib.pyplot as plt

class lattice:
    rnd.seed(time.time())
    __lowlim = -10
    __uplim = 10
    __N = 1000

    def action(self, pos):
        r = rnd.uniform(0.0, 1.0)
        if (r >= 0 and r < 0.5):
            pos -= 1
        else:
            pos += 1

        return pos
        
    def iterations(self):
        x = 0
        count = 0
        position = []
        Time = []
        while (count <= self.__N):
            position.append(x)
            Time.append(count)
            val  = self.action(x)
            if (val < self.__lowlim):
                x = val + 2
            elif (val > self.__uplim):
                x = val - 2
            else:
                x = val
            count += 1
        
        graph = [position, Time]

        return graph
        
    def single(self):
        graph = self.iterations()
        plt.title("Plot of position vs time of 1D random walker", fontdict={'family':'Times new Roman', 'color':'red', 'size':30})
        plt.xlabel("time in seconds", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        plt.ylabel("x position in meters", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        # plt.ylim(-10, 10)
        plt.grid(True, color='gray', linewidth=1.5)
        plt.plot(graph[1], graph[0], color='green', linewidth=2)
        plt.show()        

    def trajectories(self):
        graphs = []
        for i in range(0, 1000):
            graph = self.iterations()
            graphs.append(graph)

        return graphs
    
    def multiple(self):
        graphs = self.trajectories()
        plt.title("Plot of position vs time of 1D random walker for multiple trajectories", fontdict={'family':'Times new Roman', 'color':'red', 'size':30})
        plt.xlabel("time in seconds", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        plt.ylabel("x position in meters", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        # plt.ylim(-10, 10)
        plt.grid(True, color='gray', linewidth=2)
        
        for j in range(len(graphs)):
            plt.plot(graphs[j][1], graphs[j][0], linewidth=2)

        plt.show()

    def calculations(self):
        graphs = self.trajectories()
        sum = 0
        sqsum = 0
        for k in range(0, len(graphs)):
            sum += graphs[k][0][len(graphs[k][0]) - 1]
            sqsum += pow((graphs[k][0][len(graphs[k][0]) - 1]),2)
        
        mean = sum/len(graphs)
        sqmean = sqsum/len(graphs)
        means = [mean, sqmean]
        return means

    def distribution(self):
        graphs = self.trajectories()
        frequencies = []
        for l in range(0, len(graphs)):
            frequencies.append(graphs[l][0][-1])

        plt.title("Distribution of position of 1D random walk", fontdict={'family':'Times new Roman', 'color':'red', 'size':30})
        plt.xlabel("displacement in meters from center", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        plt.ylabel("frequency of 1D random walker", fontdict={'family':'Times new Roman', 'color':'black', 'size':18})
        plt.grid(True, color='gray', linewidth=1.5)
        plt.hist(frequencies, bins=20, color='green', edgecolor='black')
        plt.show()   
    
print("This program plots the graph of position of a random walker in a 1D lattice")
obj = lattice()
obj.single()
obj.multiple()
means = obj.calculations()

print(f"The first moment is {means[0]} and the second moment is {means[1]} and the distribution is...")
obj.distribution()