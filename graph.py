import matplotlib.pyplot as plt
import numpy as np

## Create functions and set domain length
x = np.arange(-1, 3, 0.01)

plt.plot(x, x**3 - 3*(x**2) + 2*x)
plt.plot(0.39, 0.375, 'or')
plt.plot(1.58, -0.4, 'og')
plt.text(0.46, 0.375, '<- Max')
plt.text(1.71, -0.42, '<- Min')

## Configure the graph
plt.title('y = x^3-3x^2 + 2x')
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim([-2, 2])
plt.grid(True)
#plt.legend(['y = x^2', 'y = 2x'], loc='upper left')

## Show the graph
#plt.savefig()
plt.show()
