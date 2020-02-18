from matplotlib.pyplot import subplot, figure
import csv
import math
import decimal
import pprint as pp
import numpy as np
import pandas as pd
from numpy import genfromtxt

profiles = pd.read_csv('profiles.csv')
result_a = profiles.replace(to_replace = 'angle', value = 100000000)
result_a.to_csv('training.csv',index=True)

def firstandlast(file):
  data = genfromtxt(file, delimiter=',')
  x = data[:,1]
  y = data[:,2]
  x_new = x.copy()
  y_new = y.copy()
  k=0
  for i in np.arange(0, len(x)):
     if (x[i] == 100000000): 
      if (x[i+1] > -3.1):
       k=k+1
       x_new = np.insert(x_new,i+k, -math.pi, axis=0)
       y_new = np.insert(y_new,i+k,(y[i+1]), axis=0) 
     if (x[i] < 3.0): 
      if (x[i+1] == 100000000):
       k=k+1
       x_new = np.insert(x_new, i+k, (31/32)*math.pi, axis=0)
       y_new = np.insert(y_new, i+k,(y[i]))
  final_data = np.zeros((len(x_new),2))
  final_data[:,0] = x_new
  final_data[:,1] = y_new
  
  return(final_data)
  
A=firstandlast('training.csv')
df = pd.DataFrame(A)
df.to_csv('training.csv', header = False, index= False)
B = pd.read_csv('training.csv')
result_b = B.replace(to_replace = 100000000, value = 'angle')
dfnew = pd.DataFrame(result_b)
dfnew.to_csv('training.csv', header = True, index= False)

def newdata(file):
 data = genfromtxt(file, delimiter=',', dtype=float)
 x = data[:,0]
 y = data[:,1]
 x_new = x.copy()
 y_new = y.copy()
 j=0
 
 
 for i in np.arange(0, len(x)):
    difference=(np.diff(x[i:i+2]))
    if difference > 0.1 and difference < 0.2:
        j=j+1
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(sum(y[i:i+2])/2))  # for single gap statement
    if difference > 0.2 and difference <0.3:
        j=j+1
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/3))  # for double gap statement
        j=j+1
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/3))  
    if difference > 0.3 and difference <0.4:
        j=j+1       
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/4)) #triple gap statement
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/4))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+3*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+3*np.diff(y[i:i+2])/4))
    if difference > 0.4 and difference <0.5:
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/5))
        j=j+1       
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/5))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+3*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+3*np.diff(y[i:i+2])/5))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+4*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+4*np.diff(y[i:i+2])/5))
    if difference > 0.5 and difference <0.6:
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/6))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/6))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+3*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+3*np.diff(y[i:i+2])/6))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+4*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+4*np.diff(y[i:i+2])/6))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+5*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+5*np.diff(y[i:i+2])/6))    
    if difference > 0.6 and difference < 0.7:
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+np.diff(y[i:i+2])/7))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+2*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+2*np.diff(y[i:i+2])/7))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+3*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+3*np.diff(y[i:i+2])/7))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+4*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+4*np.diff(y[i:i+2])/7))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+5*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+5*np.diff(y[i:i+2])/7))
        j=j+1        
        x_new = np.insert(x_new,i+j,(x[i])+6*math.pi/32)
        y_new = np.insert(y_new,i+j,(y[i]+6*np.diff(y[i:i+2])/7))  
    

 new_data = np.zeros((len(x_new),2))
 new_data[:,0] = x_new
 new_data[:,1] = y_new

 return(new_data)
C=newdata('training.csv')
df_final = pd.DataFrame(C)
df_final.to_csv('training.csv', header = False)

def labelling(file):
   data = genfromtxt(file, delimiter=',')
   x = data[:,1]
   y = data[:,2]
   index = data[:,0]
   x_new = x.copy()
   y_new = y.copy()
   n=195
   o=(221*196)-1
   p=(411*196)-1
   z=(195*590)-(196*410)
   x_new=np.insert(x_new, range(n, len(x)-(370*195)+1, n), 2)
   y_new=np.insert(y_new, range(n, len(y)-(370*195)+1, n), 2)  
   x_new=np.insert(x_new, range(o, len(x)-(z)+1, n), 1)
   y_new=np.insert(y_new, range(o, len(y)-(z)+1, n), 1)  
   x_new=np.insert(x_new, range(p, len(x)+591, n), 0)
   y_new=np.insert(y_new, range(p, len(y)+591, n), 0)  
   new_data = np.zeros((len(x_new),2))
   new_data[:,0] = x_new
   new_data[:,1] = y_new

   return(new_data)
D=labelling('training.csv')
df_fin = pd.DataFrame(D)
df_fin.to_csv('training2.csv', header = False)
#finalindexing = pd.read_csv('training.csv', names=["Index", "Angle", "Value"])
#finalindexing.to_csv('training.csv',index=False)

def reshape(file):
 data = genfromtxt(file, delimiter=',')
 newdata = np.zeros((196,int(len(data)/196)))
 j=0
 k=0
 values = data[:,2]
 for i in range(len(data)):
     if i % 196 ==0 and i != 0:
         j=j+1
         k=0
     newdata[k,j]=values[i]
     k=k+1

 return(newdata)


E=reshape('training2.csv')  
df_finish = pd.DataFrame(E)
df_finish.to_csv('final.csv', index=False, header=False)
pd.read_csv('final.csv', header=None).T.to_csv('finaltransposed.csv', header=True, index=False)


cols_to_remove = [0, 65, 130] # Column indexes to be removed (starts at 0)

cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
row_count = 0 # Current amount of rows processed

with open('finaltransposed.csv', "r") as source:
    reader = csv.reader(source)
    with open('finalfinal.csv', "w", newline='') as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)

profiles = pd.read_csv('finalfinal.csv')
profiles.replace([0,1,2],['sphere','cylinder', 'cuboid'],inplace=True)
profiles.to_csv('finalfinal.csv', header=False, index=False)