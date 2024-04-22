import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)

y1 = x**2 - 10
y2 = x**3 + x - 100
y3 = x**10 - x**8 + x**2 - 8
y4 = x**4 + x**3 + x**2 + 1
y5 = x**2 + x + 10 / 2*x
y6 = np.sin(x) / 3*x
y7 = x**3 + 2*x**2 - 10*x + 3
y8 = np.cos(x) / 5*x
y9 = x**3 / 2*x - 10*x
y10 = x+2 * x+3 * x-4

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(x, y7)
plt.plot(x, y8)
plt.plot(x, y9)
plt.plot(x, y10)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()