import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
# Plot some data on the axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], label='label1', marker="v")
# Plot some data on the axes.
ax.plot([1, 2, 3, 4], [1, 2, 3, 4], label='y=x', marker='p')
ax.scatter([2], [2], marker="o")
ax.set_title("log")
ax.legend()
ax.grid()
ax.axis([0.25, 0.5, 0.75, 1])
plt.show()
