import numpy as np
from scipy.stats import norm
import math
import csv_reader

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

with open('hw03.csv', 'r') as myFile:
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
			n0 += 1
m1T = np.mean(np.array(l1T))
m2T = np.mean(np.array(l2T))
m3T = np.mean(np.array(l3T))
m4T = np.mean(np.array(l4T))
m5T = np.mean(np.array(l5T))
m6T = np.mean(np.array(l6T))
m7T = np.mean(np.array(l7T))
m8T = np.mean(np.array(l8T))

m1F = np.mean(np.array(l1F))
m2F = np.mean(np.array(l2F))
m3F = np.mean(np.array(l3F))
m4F = np.mean(np.array(l4F))
m5F = np.mean(np.array(l5F))
m6F = np.mean(np.array(l6F))
m7F = np.mean(np.array(l7F))
m8F = np.mean(np.array(l8F))

v1T = np.std(np.array(l1T))
v2T = np.std(np.array(l2T))
v3T = np.std(np.array(l3T))
v4T = np.std(np.array(l4T))
v5T = np.std(np.array(l5T))
v6T = np.std(np.array(l6T))
v7T = np.std(np.array(l7T))
v8T = np.std(np.array(l8T))

v1F = np.std(np.array(l1F))
v2F = np.std(np.array(l2F))
v3F = np.std(np.array(l3F))
v4F = np.std(np.array(l4F))
v5F = np.std(np.array(l5F))
v6F = np.std(np.array(l6F))
v7F = np.std(np.array(l7F))
v8F = np.std(np.array(l8F))


za = norm.ppf(0.05,0,1)
i_o1 = math.sqrt((math.pow(v1F,2)/n0)+(math.pow(v1T,2)/n1))
z1 = ((m1T-m1F)/i_o1)
i_o2 = math.sqrt((math.pow(v2F,2)/n0)+(math.pow(v2T,2)/n1))
z2 = ((m2T-m2F)/i_o2)
i_o3 = math.sqrt((math.pow(v3F,2)/n0)+(math.pow(v3T,2)/n1))
z3 = ((m3T-m3F)/i_o3)
i_o4 = math.sqrt((math.pow(v4F,2)/n0)+(math.pow(v4T,2)/n1))
z4 = ((m4T-m4F)/i_o4)
i_o5 = math.sqrt((math.pow(v5F,2)/n0)+(math.pow(v5T,2)/n1))
z5 = ((m5T-m5F)/i_o5)
i_o6 = math.sqrt((math.pow(v6F,2)/n0)+(math.pow(v6T,2)/n1))
z6 = ((m6T-m6F)/i_o6)
i_o7 = math.sqrt((math.pow(v7F,2)/n0)+(math.pow(v7T,2)/n1))
z7 = ((m7T-m7F)/i_o7)
i_o8 = math.sqrt((math.pow(v8F,2)/n0)+(math.pow(v8T,2)/n1))
z8 = ((m8T-m8F)/i_o8)

'''
print (abs(za)-abs(z1))
print (abs(za)-abs(z2))
print (abs(za)-abs(z3))
print (abs(za)-abs(z4))
print (abs(za)-abs(z5))
print (abs(za)-abs(z6))
print (abs(za)-abs(z7))
print (abs(za)-abs(z8))
'''
#print (l1F[0:10])

i11T = m1T-(v1T/(math.sqrt(n1)))
i12T = m1T+(v1T/(math.sqrt(n1)))
i21T = m2T-(v2T/(math.sqrt(n1)))
i22T = m2T+(v2T/(math.sqrt(n1)))
i31T = m3T-(v3T/(math.sqrt(n1)))
i32T = m3T+(v3T/(math.sqrt(n1)))
i41T = m4T-(v4T/(math.sqrt(n1)))
i42T = m4T+(v4T/(math.sqrt(n1)))
i51T = m5T-(v5T/(math.sqrt(n1)))
i52T = m5T+(v5T/(math.sqrt(n1)))
i61T = m6T-(v6T/(math.sqrt(n1)))
i62T = m6T+(v6T/(math.sqrt(n1)))
i71T = m7T-(v7T/(math.sqrt(n1)))
i72T = m7T+(v7T/(math.sqrt(n1)))
i81T = m8T-(v8T/(math.sqrt(n1)))
i82T = m8T+(v8T/(math.sqrt(n1)))


i11F = m1F-(v1F/(math.sqrt(n0)))
i12F = m1F+(v1F/(math.sqrt(n0)))
i21F = m2F-(v2F/(math.sqrt(n0)))
i22F = m2F+(v2F/(math.sqrt(n0)))
i31F = m3F-(v3F/(math.sqrt(n0)))
i32F = m3F+(v3F/(math.sqrt(n0)))
i41F = m4F-(v4F/(math.sqrt(n0)))
i42F = m4F+(v4F/(math.sqrt(n0)))
i51F = m5F-(v5F/(math.sqrt(n0)))
i52F = m5F+(v5F/(math.sqrt(n0)))
i61F = m6F-(v6F/(math.sqrt(n0)))
i62F = m6F+(v6F/(math.sqrt(n0)))
i71F = m7F-(v7F/(math.sqrt(n0)))
i72F = m7F+(v7F/(math.sqrt(n0)))
i81F = m8F-(v8F/(math.sqrt(n0)))
i82F = m8F+(v8F/(math.sqrt(n0)))

l11 = []
l12 = []
l21 = []
l22 = []
l31 = []
l32 = []
l41 = [] 
l42 = []
l51 = []
l52 = []
l61 = []
l62 = []
l71 = []
l72 = []
l81 = []
l82 = []
i = 1
while i <= 10000:
	a = np.random.choice(l1T+l1F,n1+n0,replace=True)
	l11.append(np.mean(a))
	l12.append(np.median(a))
	a = np.random.choice(l2T+l2F,n1+n0,replace=True)
	l21.append(np.mean(a))
	l22.append(np.median(a))
	a = np.random.choice(l3T+l3F,n1+n0,replace=True)
	l31.append(np.mean(a))
	l32.append(np.median(a))
	a = np.random.choice(l4T+l4F,n1+n0,replace=True)
	l41.append(np.mean(a))
	l42.append(np.median(a))
	a = np.random.choice(l5T+l5F,n1+n0,replace=True)
	l51.append(np.mean(a))
	l52.append(np.median(a))
	a = np.random.choice(l6T+l6F,n1+n0,replace=True)
	l61.append(np.mean(a))
	l62.append(np.median(a))
	a = np.random.choice(l7T+l7F,n1+n0,replace=True)
	l71.append(np.mean(a))
	l72.append(np.median(a))
	a = np.random.choice(l8T+l8F,n1+n0,replace=True)
	l81.append(np.mean(a))
	l82.append(np.median(a))
	i += 1
m11 =  np.mean(np.array(l11))
s11 =  np.std(np.array(l11))
m21 =  np.mean(np.array(l21))
s21 =  np.std(np.array(l21))
m31 =  np.mean(np.array(l31))
s31 =  np.std(np.array(l31))
m41 =  np.mean(np.array(l41))
s41 =  np.std(np.array(l41))
m51 =  np.mean(np.array(l51))
s51 =  np.std(np.array(l51))
m61 =  np.mean(np.array(l61))
s61 =  np.std(np.array(l61))
m71 =  np.mean(np.array(l71))
s71 =  np.std(np.array(l71))
m81 =  np.mean(np.array(l81))
s81 =  np.std(np.array(l81))

m12 =  np.mean(np.array(l12))
s12 =  np.std(np.array(l12))
m22 =  np.mean(np.array(l22))
s22 =  np.std(np.array(l22))
m32 =  np.mean(np.array(l32))
s32 =  np.std(np.array(l32))
m42 =  np.mean(np.array(l42))
s42 =  np.std(np.array(l42))
m52 =  np.mean(np.array(l52))
s52 =  np.std(np.array(l52))
m62 =  np.mean(np.array(l62))
s62 =  np.std(np.array(l62))
m72 =  np.mean(np.array(l72))
s72 =  np.std(np.array(l72))
m82 =  np.mean(np.array(l82))
s82 =  np.std(np.array(l82))


b1s = m11-s11
b1b = m11+s11
b2s = m21-s21
b2b = m21+s21
b3s = m31-s31
b3b = m31+s31
b4s = m41-s41
b4b = m41+s41
b5s = m51-s51
b5b = m51+s51
b6s = m61-s61
b6b = m61+s61
b7s = m71-s71
b7b = m71+s71
b8s = m81-s81
b8b = m81+s81

'''

print ("{},{}".format(b1s,b1b))
print ("{},{}".format(b2s,b2b))
print ("{},{}".format(b3s,b3b))
print ("{},{}".format(b4s,b4b))
print ("{},{}".format(b5s,b5b))
print ("{},{}".format(b6s,b6b))
print ("{},{}".format(b7s,b7b))
print ("{},{}".format(b8s,b8b))
'''

b21s = m12-s12
b21b = m12+s12
b22s = m22-s22
b22b = m22+s22
b23s = m32-s32
b23b = m32+s32
b24s = m42-s42
b24b = m42+s42
b25s = m52-s52
b25b = m52+s52
b26s = m62-s62
b26b = m62+s62
b27s = m72-s72
b27b = m72+s72
b28s = m82-s82
b28b = m82+s82


'''
print ("{},{}".format(b1s,b1b))
print ("{},{}".format(b2s,b2b))
print ("{},{}".format(b3s,b3b))
print ("{},{}".format(b4s,b4b))
print ("{},{}".format(b5s,b5b))
print ("{},{}".format(b6s,b6b))
print ("{},{}".format(b7s,b7b))
print ("{},{}".format(b8s,b8b))
'''

'''
print (m11/s11)
print (m21/s21)
print (m31/s31)
print (m41/s41)
print (m51/s51)
print (m61/s61)
print (m71/s71)
print (m81/s81)
'''

print (m12/s12)
print (m22/s22)
print (m32/s32)
print (m42/s42)
print (m52/s52)
print (m62/s62)
print (m72/s72)
print (m82/s82)








		     
		
