import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
i=68706
ax.annotate(str(i), xy=(2, 1), xytext=(2, 1.001), arrowprops=dict(facecolor='red', shrink=0.1), )
ax.set_ylim(-2,2)
plt.show()

