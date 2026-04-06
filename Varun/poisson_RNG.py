import numpy.random as rnd
import seaborn as sns
import matplotlib.pyplot as plt

X = []
for i in range (0,10000):
    r = rnd.poisson(5000)
    X.append(r)
sns.histplot(X, bins=100, stat="probability")
plt.xlabel('Number', color = 'red')
plt.ylabel('Probability', color = 'red')
plt.title('Poisson Distribution Random Number Generator', color = 'green')
plt.show()