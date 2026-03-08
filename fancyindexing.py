import numpy as np

variable =np.zeros((10,10),dtype="int")
print(variable)
print(variable.shape)
print(variable.shape[0])
row = variable.shape[0]
for i in range(row):
    variable[i] = i

print(variable)

list1 = [1,3,5,7]

print(variable[list1])

list2 =[8,5,2,7,3]
print(variable[list2])
 
example = np.arange(1,17).reshape((4,4))
print(example)
example[[0,3],[1,2]]
print(example[[0,3],[1,2]])      

rows = [0,2,3,1]
columns = [3,0,2,1]
example[rows,columns]
print(example[rows,columns])