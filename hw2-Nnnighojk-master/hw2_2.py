import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('hw02_problem2c.csv')

stats.probplot(data, dist = 'rayleigh', plot=plt)
plt.show() # modify this to write the plot to a file instead
#plt.savefig('plot2_13.png')
