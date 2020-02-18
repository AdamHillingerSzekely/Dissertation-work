import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot, figure
import csv
from numpy import genfromtxt
profiles = pd.read_csv('training.csv')
profiles.to_csv('new.csv', header = False, index= False)
cols_to_remove = [0,1] # Column indexes to be removed (starts at 0)

cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
row_count = 0 # Current amount of rows processed

with open('new.csv', "r") as source:
    reader = csv.reader(source)
    with open('values.csv', "w", newline='') as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)
df = pd.read_csv("values.csv")
#checking the number of empty rows in th csv file
df.isnull().sum()
#Droping the empty rows
modifiedDF = df.dropna()
#Saving it to the csv file 
modifiedDF.to_csv('values.csv',index=False)
with open('loop.csv','w') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    n=16
    data = genfromtxt('values.csv', delimiter=',', dtype=float)
    for i in range(0, len(data), n): 
      ynewzero=((sum(data[i:i+n]))/n)
      row = [ynewzero]
      writer.writerow(row)
    
def means(file):
 n=16
 data = genfromtxt(file, delimiter=',')
 newdata = np.zeros((590,int(192/n)))
 j=0
 k=0
 for i in range(len(data)):
     if i % int(192/n) ==0 and i != 0:
         j=j+1
         k=0
     newdata[j,k]=data[i]
     k=k+1
 return(newdata)
     
C=means('loop.csv')
df_final = pd.DataFrame(C)
df_final.to_csv('loopsfinal.csv', header = False, index = False)

s = [2]*220  
ss= [1]*190
sss=[0]*180
h=np.concatenate((s,ss,sss),axis=0)

data = genfromtxt('loopsfinal.csv', delimiter=',')
x= np.insert(data,12,h,axis = 1)
dffinal = pd.DataFrame(x)
dffinal.to_csv('loopsfinals.csv', header = False, index = False)
profiles = pd.read_csv('loopsfinals.csv')
profiles.replace([0,1,2],['sphere','cylinder', 'cuboid'],inplace=True)
profiles.to_csv('work12.csv', header=False, index=False)
