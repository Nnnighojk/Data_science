import numpy as np
from helper import plotHisto
import matplotlib.pyplot as plt

def sampleMean(data,k):
	d = np.random.choice(data, k, replace=False)
	ans = np.mean(d)
	return (ans)

data1 = np.loadtxt('hw02_problem2a.csv')
#i1 = 0
#l1 = []
#for i1 in range(10000):
#	l1.append(sampleMean(data1,100))
#print (len(l1))
#plt.hist(l1)
#plt.savefig('plotb_1.png')

data2 = np.loadtxt('hw02_problem2b.csv')
#i2 = 0
#l2 = []
#for i2 in range(10000):
#	l2.append(sampleMean(data2,100))
#print (len(l2))
#plt.hist(l2)
#plt.savefig('plotb_2.png')

data3 = np.loadtxt('hw02_problem2c.csv')
#i3 = 0
#l3 = []
#for i3 in range(10000):
#	l3.append(sampleMean(data3,100))
#print (len(l3))
#plt.hist(l3)
#plt.savefig('plotb_3.png')
print (np.mean(data1))
print (np.mean(data2))
print (np.mean(data3))
	
