import numpy.random as rnd
import seaborn as sns
import matplotlib.pyplot as plt

X = []
for i in range (0,10000):
    r = rnd.exponential()
    X.append(r)
sns.histplot(X, bins=30, stat="probability")
plt.xlabel('Number', color = 'red')
plt.ylabel('Probability', color = 'red')
plt.title('Exponential Distribution Random Number Generator', color = 'green')
plt.show()