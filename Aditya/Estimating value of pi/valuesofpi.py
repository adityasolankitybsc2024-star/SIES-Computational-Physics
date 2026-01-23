import random as rnd
import time
import math

class calculatepi:
    rnd.seed(time.time())

    def pi(self, iterations):
        circle = 0
        square = 0
        for i in range(0, iterations):
            x = rnd.uniform(-1.0, 1.0)
            y = rnd.uniform(-1.0, 1.0)

            if (pow(x, 2) + pow(y, 2) <= 1):
                circle += 1
            else:
                square += 1

        pi = 4*(circle/iterations)

        return pi

    def fileprint(self):
        iterations = [500, 5000, 50000, 500000, 10000000]
        pivalues = []

        for i in range(0, len(iterations)):
            pivalues.append(self.pi(iterations[i]))

        try:
            with open("C:/Users/lenovo/OneDrive/Desktop/Coding/SIES Python/sem 2 practice RW/Estimating value of pi/pitable.txt", "w") as file:
                if (file):
                    file.write(f"|Iterations   |   Pi Values|   Absolute Error|   Relative Error|   Percentage Error|\n")
                    for j in range(0, len(iterations)):
                        file.write(f"|{iterations[j]:<13}| {pivalues[j]:^11.6f}| {abs(pivalues[j]-math.pi):^16.6f}| {(abs(pivalues[j]-math.pi)/math.pi):^16.6f}| {((abs(pivalues[j]-math.pi)/math.pi)*100):>17.6f}%|\n")
                    file.write(f"\nThe actual value of pi is {math.pi:.6f}")

        except IOError as e:
            print("File error:", e)

print("This function prints the values of pi for different lengths of iterations.")
obj = calculatepi()
obj.fileprint()