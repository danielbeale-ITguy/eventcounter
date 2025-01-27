import matplotlib.pyplot as plt
import numpy as np
from eventsorter import count
dansdict = count






names = list(dansdict.keys())
Age = list(dansdict.values())


plt.figure(figsize=(16,9))
plt.bar(    names,Age)
plt.ylabel('Events Over Time')
plt.xticks(rotation = 90)
plt.xticks(size=8)
plt.ylim(0, 1000)
# Save the plot to a file
plt.savefig('plot.png')  # Saves the plot as a PNG file
