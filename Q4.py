import numpy as np
bat1=[]
bat2=[]
bat3=[]
arr1=[1,2,0,0,4,1,6,2,1,3]
bat1=arr[0]
if  bat1 %2 !=0:
    for i in range(len(arr1)):
        if arr[1] %2==0:
            x=arr1[i]
            bat2.append(x)
        else:
            y=arr1[i]
            bat1=y
            bat3.append(y)
            print(bat3)
else:
    for i in range(len(arr1)):
        if arr1[i] %2==0:
            x=arr1[i]
            bat3.append(x)
        else:
            y=arr1[i]
            bat1=y
            bat2.append(y)
print(bat2,bat3)
print(sum(bat2),sum(bat3))