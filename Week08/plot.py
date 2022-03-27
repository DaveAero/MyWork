# lab8.1.2-plot.py
# This program is used to deomstrate plots
# author: David Burke

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
