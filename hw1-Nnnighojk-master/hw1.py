import numpy as np
import matplotlib.pyplot as plt
from helper import plotHisto

#INPUTS
#data: list of data points
#numbins: number of bins in the output histogram
#minimum: the minimum value of the histogram range
#maximum: the maximum value of the histogram range
#
#RETURNS:
#histo: a list of length numbins, with each entry containing the number of data points in the corresponding histogram bin
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def buildHisto (data, numbins, minimum, maximum):
	l = zerolistmaker(numbins)
	for i in data:
		a = 0
		b = (maximum-minimum)/numbins
		c = 1
		index = 0
		while c <= numbins:
			 if i >= a and i < b:
            			l[index] += 1
        		 a += (maximum-minimum)/numbins 
        		 b += (maximum-minimum)/numbins
        	         index += 1
        		 c += 1
	histo = l  
	return histo

data = np.loadtxt('math_scores.txt')
data1 = np.random.choice(data, 5000, replace=False)

# 2. Build and plot histogram with 10 bins
histo = buildHisto(data, 10, 0.0, 100.0)
plotHisto(histo, 'histo1.png', 0.0, 100.0)

# 3. Build and plot histogram with 200 bins
histo = buildHisto(data, 200, 0.0, 100.0)
plotHisto(histo, 'histo2.png', 0.0, 100.0)

histo = buildHisto(data, 150, 0.0, 100.0)
plotHisto(histo, 'histo3.png', 0.0, 100.0)

histo = buildHisto(data1, 150, 0.0, 100.0)
plotHisto(histo, 'histo4.png', 0.0, 100.0)

histo = buildHisto(data1, 1000, 0.0, 100.0)
plotHisto(histo, 'histo6.png', 0.0, 100.0)

histo = buildHisto(data, 156, 0.0, 100.0)
plotHisto(histo, 'histo5.png', 0.0, 100.0)
	
