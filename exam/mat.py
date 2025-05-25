import matplotlib.pyplot as plt
import math
import numpy as np
x = np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sin values")
plt.show()