import numpy as np
arr_rand=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
print(arr_rand)
uniqs,counts=np.unique(arr_rand,return_counts=True)
print("Unique Items:",uniqs)
 bprint("Counts:",counts)