#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot, figure
import csv
import math
import decimal
import pprint as pp
import numpy as np
from numpy import genfromtxt

def newdata(file):
 data = genfromtxt(file, delimiter=',',skip_header=1)
 x = data[:,0]
 y = data[:,1]
 x_new = x.copy()
 y_new = y.copy()
 j=0

 for i in np.arange(0, len(x)):
    difference=(np.diff(x[i:i+2]))
    if difference > 0.1 and difference < 0.2:
        
        j = j+1
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(sum(y[i:i+2])/2))  # for single gap
    if difference > 0.2:
        j = j+1
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/3))  # for double gap
        j = j+1
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/3))  


 new_data = np.zeros((len(x_new),2))
 new_data[:,0] = x_new
 new_data[:,1] = y_new
 return(new_data)

A=newdata('profile_0.csv')
B=newdata('profile_1.csv')
C=newdata('profile_2.csv')


def meanvalues(q,n,k):

 x= q[:,0]
 y= q[:,1]
 xnewzero = np.zeros(int(len(x)/n))
 ynewzero = np.zeros(int(len(y)/n))

#print('The average x values taking the mean over ' + str(n) + ' points are ' )
 for i in np.arange(0, len(x), n):
  xnewzero[int(i/n)]= ((sum(x[i:i+n]))/n)+ k*math.pi
  ynewzero[int(i/n)]= (sum(y[i:i+n]))/n
  finaldata = np.zeros((len(xnewzero),2))
  finaldata[:,0] = xnewzero 
  finaldata[:,1] = ynewzero 
 
 return(finaldata)

px=meanvalues(A,1,1)
py=meanvalues(B,1,1)
pz=meanvalues(C,1,1)
finaltrace = np.concatenate((px, py, pz))
print(px)
print(py)
print(pz)
fig = plt.figure()
x1 = px[:,0]
y1 = px[:,1]
x2 = py[:,0]
y2 = py[:,1]
x3 = pz[:,0]
y3 = pz[:,1]



plt.subplot(3, 1, 1)
plt.plot(x1, y1)
plt.xlabel('Angle')
plt.ylabel('Value')
plt.subplot(3, 1, 2)
plt.plot(x2, y2)
plt.xlabel('Angle')
plt.ylabel('Value')
plt.subplot(3, 1, 3)
plt.plot(x3, y3)

plt.xlabel('Angle')
plt.ylabel('Value')
plt.legend()
plt.show()
  


  
