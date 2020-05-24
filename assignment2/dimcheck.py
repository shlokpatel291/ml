import numpy as np 
arr1=np.array([1,2,3,4,5,6,7,8,9,10,11])
arr2=[]
for i in range(0,len(arr1)):
    if i%2==0:
        arr2.insert(arr1[i])
print(arr2)

arr3=arr2.reshape(2,-1)
print(arr3)
print(arr3.ndim)