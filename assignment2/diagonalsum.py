import numpy as np
arr=[[1,2,3],[4,5,6],[7,8,9]]
total=0
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if i==j:
            total+=arr[i][j]


print(total)
    

    
