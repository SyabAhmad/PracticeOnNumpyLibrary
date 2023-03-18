import numpy as np
data = np.full([3,3], 5)
print(data)

data1 = np.full([5,5], 9)
print(data1)

data1[1:4, 1:4] = 0
print(data1)

data1[2,2] = 9
print(data1)
