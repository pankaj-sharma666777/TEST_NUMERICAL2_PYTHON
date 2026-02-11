import numpy as np
array = np.array([1,3,5,50,2,4,6,7])
print(np.split(array,[3,5]))
x,y,z =np.split(array,[3,5])
print(x)
print(y)
print(z)


print(np.split(array,[4]))
print(np.split(array,4))
