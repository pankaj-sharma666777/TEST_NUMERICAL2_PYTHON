import numpy as np
array_1 = np.random.randint(1,500,15)
print(array_1)
array_2 =array_1.reshape(3,5)
print(array_2)
index_value = np.argpartition(array_1,-5)[-5:]
print(index_value)

print(np.sort(array_1[index_value]))

index_value_2 =np.argpartition(array_2,-3,axis=0)[-5:]
print(index_value_2)

print(np.sort(array_2[index_value_2]))

index_value_3 =np.argpartition(array_2.ravel(),-5)[-5:]
print(index_value_3)
print(index_value)
# print(array_2[index_value_3])    ----->error

index_value_3_unraveled = np.unravel_index(index_value_3 ,array_2.shape)
print(array_2[index_value_3_unraveled])
print(array_1[index_value])


# allclose function

# print(np.allclose(array_1,array_2,0.1))
array_3 =np.array([0.12,0.17,0.24,0.29,0.33])
array_4 = np.array([0.13,0.19,0.26,0.31,0.33])
x = np.allclose(array_3,array_4,0.1)
print(x)

x2 = np.allclose(array_3,array_4,0.2)
print(x2)