import numpy as np 
arr1=np.array([1,2,3,4,5,6,7])
arr2=[]
for i in range(0,len(arr1)):
    if i%2==0:
        arr2.append(arr1[i])
print(arr2)
