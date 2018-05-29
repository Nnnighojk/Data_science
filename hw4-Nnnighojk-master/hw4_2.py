import numpy as np
import matplotlib.pyplot as plt

x_google = []
google = []
with open('google_stock_train.txt', 'r') as myFile:
        line=myFile.readlines()
	for item in line:
		google.append(item.strip())
for i in range(175):
	l_1 = []
	l_1 = google[i:i+25]
	l_1 = list(reversed(l_1))
	x_google.append(l_1)
#print (x_google[174])
xg_l = x_google
x_nvs = []
nvs = []
with open('nvs_stock_train.txt', 'r') as myFile:
        line=myFile.readlines()
	for item in line:
		nvs.append(item.strip())
for i in range(175):
	l_2 = []
	l_2 = nvs[i:i+25]
	l_2 = list(reversed(l_2))
	x_nvs.append(l_2)
xn_l = x_nvs
#print (x_nvs[174])
#x_later = x_google
#print (x_later)
x_google = np.matrix(x_google, dtype = np.float32)
x_nvs = np.matrix(x_nvs, dtype = np.float32)

#print (x_google.T.shape)

y_google = list(google[25:200])
y_google = np.matrix(y_google, dtype = np.float32)
y_google = y_google.T
#print (y_google) 
y_nvs = list(nvs[25:200])
y_nvs = np.matrix(y_nvs, dtype = np.float32)
y_nvs = y_nvs.T
#print (y_google.shape) 
#print (x_google)

b1 = (x_google.T)*(x_google)
b2 = b1.I
b3 = b2*x_google.T
beta_google = b3*y_google
#print (beta_google)

b1_2 = (x_nvs.T)*(x_nvs)
b2_2 = b1_2.I
b3_2 = b2_2*x_nvs.T
beta_nvs = b3*y_nvs
print (beta_nvs)

lg = []
lg = list(reversed(google[175:200]))

yg_new = [] 

ln = []
ln = list(reversed(nvs[175:200]))

yn_new = [] 

for i in range(151,181):
	a = np.array(beta_google.T)[0]
	b = np.array(lg, dtype = np.float32)
	c = (sum(list(a*b)))
	d = np.array(y_google.T[0])
	d = list(d[0])
	d.append(c)

	yg_new.append(c)
	y_google = np.matrix(d, dtype = np.float32)
	y_google = y_google.T

	lg = list(reversed(list(d[151:176])))
	xg_l.append(lg)
	x_google = np.matrix(xg_l, dtype = np.float32)
	b1 = (x_google.T)*(x_google)
	b2 = b1.I
	b3 = b2*x_google.T
	beta_google = b3*y_google
	
	an = np.array(beta_nvs.T)[0]
	bn = np.array(ln, dtype = np.float32)
	cn = (sum(list(an*bn)))
	dn = np.array(y_nvs.T[0])
	dn = list(dn[0])
	dn.append(cn)

	yn_new.append(cn)
	y_nvs = np.matrix(dn, dtype = np.float32)
	y_nvs = y_nvs.T

	ln = list(reversed(list(dn[151:176])))
	xn_l.append(ln)
	x_nvs = np.matrix(xn_l, dtype = np.float32)
	b1_1 = (x_nvs.T)*(x_nvs)
	b2_1 = b1_1.I
	b3_1 = b2_1*x_nvs.T
	beta_nvs = b3_1*y_nvs
yn_new = [x * 10 for x in yn_new]
google = map(lambda x: float(x), google)
nvs = map(lambda x: float(x), nvs)
fig1 = plt.figure()
plt.plot(range(200),google,'r')
plt.plot(range(200,230),yg_new,'b')
plt.ylabel('google stock prices')
plt.xlabel('stock numbers')
#plt.show()
fig2 = plt.figure()
plt.plot(range(200),nvs,'g')
plt.plot(range(200,230),yn_new,'y')
plt.ylabel('nvs stock prices')
plt.xlabel('stock numbers')
#plt.show()

#print (yn_new)
	

