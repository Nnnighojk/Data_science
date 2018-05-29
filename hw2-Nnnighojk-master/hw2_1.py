import numpy as np
from helper import plotHisto
import matplotlib.pyplot as plt
#from hw1 import buildHisto

def sampleMean(data,k):
	d = np.random.choice(data, k, replace=False)
	ans = np.mean(d)
	return (ans)

data = np.loadtxt('hw02_problem1.csv')
data1 = np.random.choice(data, 10000, replace=False)
plt.hist(data1)
plt.savefig('plot5.png')
#print(sampleMean(data,5000))
i = 0
l = []
for i in range(10000):
	l.append(sampleMean(data,100))
#print (len(l))
#plt.hist(l)
#plt.savefig('plot1_5_2.png')
#plt.hist(np.mean(data))
#plt.savefig('plot1_5_3.png')	
#print (np.mean(data))




