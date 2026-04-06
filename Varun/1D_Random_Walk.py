import matplotlib.pyplot as plt
import random as rnd
import seaborn as sns
import statistics as stat
import time

rnd.seed(time.time())
distances = []
runs=10000

for run in range(1, runs):
    position = 0
    path = []
    trials = 1000
    for trial in range(1, trials):
        choice = rnd.uniform(0,1)
        if choice < 0.5:
            position -= 1
        else:
            position += 1
        path.append(position)
    distance = path[-1]
    distances.append(distance)
    plt.plot(path)
plt.show()

plt.plot(path)
plt.show()

R = stat.mean(distances)
R2 = stat.variance(distances, R)
R3 = stat.stdev(distances, R)

print(R)
print(R2)
print(R3)

fig, axes = plt.subplots(1, 2, figsize=(12,5))

sns.histplot(distances, bins=30, stat="density", ax=axes[0])
axes[0].set_title('Distribution of Final Positions (Seaborn)', color = 'green')
axes[0].set_xlabel('Final Position', color = 'red')
axes[0].set_ylabel('Probablity', color = 'red')

axes[1].hist(distances, bins=30, density=True)
axes[1].set_title('Distribution of Final Positions (Matplotlib)', color = 'green')
axes[1].set_xlabel('Final Position', color = 'red')
axes[1].set_ylabel('Probablity', color = 'red')
plt.tight_layout()
plt.show()