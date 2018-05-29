import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt

l1T = []
l2T = []
l3T = []
l4T = []
l5T = []
l6T = []
l7T = []
l8T = []
l9T = []
l1F = []
l2F = []
l3F = []
l4F = []
l5F = []
l6F = []
l7F = []
l8F = []
l9F = []
n1 = 0
n0 = 0

with open('hw04.csv', 'r') as myFile:
	line=myFile.readlines()
	for item in line[1:]:
		k = item.split(',')
		if k[10] == 'T\r\n':
			l1T.append(float(k[1]))
			l2T.append(float(k[2]))
			l3T.append(float(k[3]))
			l4T.append(float(k[4]))
			l5T.append(float(k[5]))
			l6T.append(float(k[6]))
			l7T.append(float(k[7]))
			l8T.append(float(k[8]))
			l9T.append(float(k[9]))
			n1 += 1
		else:
			l1F.append(float(k[1]))
			l2F.append(float(k[2]))
			l3F.append(float(k[3]))
			l4F.append(float(k[4]))
			l5F.append(float(k[5]))
			l6F.append(float(k[6]))
			l7F.append(float(k[7]))
			l8F.append(float(k[8]))
			l9F.append(float(k[9]))
			n0 += 1
a = sum(l9T)/len(l9T)
b = sum(l9F)/len(l9F)
l9T[:] = [x - a for x in l9T]
l9F[:] = [x - b for x in l9F]
yT = np.matrix(l9T)
yT = yT.T
yF = np.matrix(l9F)
yF = yF.T
#print (sum(l9T)/len(l9T))
#print (sum(l9F)/len(l9F))
xT = []
rowT = []
xF = []
rowF = []
for i in range(0,len(l1T)):
	rowT.append(l1T[i])
	rowT.append(l2T[i])
	rowT.append(l3T[i])
	rowT.append(l4T[i])
	rowT.append(l5T[i])
	rowT.append(l6T[i])
	rowT.append(l7T[i])
	rowT.append(l8T[i])
	xT.append(rowT)
	rowT = []
for i in range(0,len(l1F)):
	rowF.append(l1F[i])
	rowF.append(l2F[i])
	rowF.append(l3F[i])
	rowF.append(l4F[i])
	rowF.append(l5F[i])
	rowF.append(l6F[i])
	rowF.append(l7F[i])
	rowF.append(l8F[i])
	xF.append(rowF)
	rowF = []
xT = np.matrix(xT)
xF = np.matrix(xF)
l = np.array(xT.mean(0))
l2 = np.array(xF.mean(0))
l1T[:] = [x - l[0][0] for x in l1T]
l2T[:] = [x - l[0][1] for x in l2T]
l3T[:] = [x - l[0][2] for x in l3T]
l4T[:] = [x - l[0][3] for x in l4T]
l5T[:] = [x - l[0][4] for x in l5T]
l6T[:] = [x - l[0][5] for x in l6T]
l7T[:] = [x - l[0][6] for x in l7T]
l8T[:] = [x - l[0][7] for x in l8T]
l1F[:] = [x - l2[0][0] for x in l1F]
l2F[:] = [x - l2[0][1] for x in l2F]
l3F[:] = [x - l2[0][2] for x in l3F]
l4F[:] = [x - l2[0][3] for x in l4F]
l5F[:] = [x - l2[0][4] for x in l5F]
l6F[:] = [x - l2[0][5] for x in l6F]
l7F[:] = [x - l2[0][6] for x in l7F]
l8F[:] = [x - l2[0][7] for x in l8F]
xT = []
rowT = []
xF = []
rowF = []
for i in range(0,len(l1T)):
	rowT.append(l1T[i])
	rowT.append(l2T[i])
	rowT.append(l3T[i])
	rowT.append(l4T[i])
	rowT.append(l5T[i])
	rowT.append(l6T[i])
	rowT.append(l7T[i])
	rowT.append(l8T[i])
	xT.append(rowT)
	rowT = []
for i in range(0,len(l1F)):
	rowF.append(l1F[i])
	rowF.append(l2F[i])
	rowF.append(l3F[i])
	rowF.append(l4F[i])
	rowF.append(l5F[i])
	rowF.append(l6F[i])
	rowF.append(l7F[i])
	rowF.append(l8F[i])
	xF.append(rowF)
	rowF = []
xT = np.matrix(xT)
xF = np.matrix(xF)
l = np.array(xT.mean(0))
l2 = np.array(xF.mean(0))
xT_sq = np.multiply(xT,xT)
#print (xT_sq.sum(0))
xF_sq = np.multiply(xF,xF)
#print (xF_sq.sum(0))
l_b = []
s = np.logspace(-10,10,1000)
fig = plt.figure()
for i in s:
	c = xT.T*xT
	d = np.multiply(i,np.identity(8))
	y = c+d #8x8
	f = y.I #8x8
	z = xT.T*yT #8x1
	#print (yT.shape, xT.shape, z.shape)
	l_b.append(f*z) #appending 8x1
	#fig.add_subplot(plt.semilogx(s,f*z))
#print ('done')
lb_new = []
#print('l_b[i].tolist() = {}'.format(l_b[0].tolist()))
for i in range(len(l_b)):
	to_app = map(lambda x: x[0], l_b[i].tolist())
	lb_new.append(to_app)

for j in range(8):
	y_el = map(lambda x: x[j], lb_new)
	#fig.add_subplot(plt.semilogx(s,y_el))
	plt.semilogx(s,y_el)
	plt.xlabel('lamda')
	plt.ylabel('beta')
#plt.show()
l_mse = []
m = 30
for beta in lb_new:
	beta = np.matrix(beta)
	p = xF*beta.T
	q = yF - p
	r = (np.multiply(q,q))/m
	#print (r.shape)
	l_mse.append(r)
mse_new = []
for i in range(len(l_mse)):
	to_app = map(lambda x: x[0], l_mse[i].tolist())
	mse_new.append(to_app)
for j in range(8):
	y_el = map(lambda x: x[j], mse_new)
	#fig.add_subplot(plt.semilogx(s,y_el))
	plt.semilogx(s,y_el)
	plt.xlabel('lamda')
	plt.ylabel('mean squared error')
#plt.show()

	
	
	
