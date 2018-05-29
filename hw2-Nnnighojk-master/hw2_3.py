from csv_reader import readData
import matplotlib.pyplot as plt

data = readData('hw02_problem3.csv')
l1 = []
l2 = []
l3 = []
l4 = []

for i in range(len(data)):
	if data[i][1] == 'red':
		l1.append(data[i][0])
	if data[i][1] == 'green':
		l2.append(data[i][0])
	if data[i][2] == 'white':
		l3.append(data[i][0])
	if data[i][2] == 'black':
		l4.append(data[i][0])

#l = []
#for i in range(len(data)):
#	l.append(data[i][0])

#plt.hist(l)
#plt.savefig('plot3_1.png')

plt.hist(l1)
plt.savefig('plot3_21.png')
#plt.hist(l2)
#plt.savefig('plot3_22.png')
#plt.hist(l3)
#plt.savefig('plot3_23.png')
#plt.hist(l4)
#plt.savefig('plot3_24.png')
