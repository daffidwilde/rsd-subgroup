import matplotlib.pyplot as plt
import fibonacci
x = [i for i in range(11)]
y = [fibonacci.get(n) for n in x]
plt.scatter(x, y)
plt.savefig("../tex/scatter-plot-of-fibonacci-numbers.pdf")