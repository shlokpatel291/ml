from matplotlib import pyplot as plt 
import math 
import numpy as np 
x=[]
y=[]
for i in range(1,11):
    x=np.append(x,i)
    p=math.log(i)
    y=np.append(y,p)

plt.scatter(x,y)

plt.show()