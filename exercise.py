import numpy as np
array_r_1 = np.random.randint(1,150,20)
print(array_r_1)

print(array_r_1.sum())
print(array_r_1.max())
print(array_r_1.min())
print(array_r_1.mean())
array_2 =np.arange(1,60,3)
print(array_2)

print(f"sum of both array {array_2+array_r_1}")
print(f"array_r_1{array_r_1}")
print(f"arguement at 10th index {array_r_1[10]}")
print(f"any random element {array_r_1[np.random.randint(1,21,1)]}")

r_element = array_r_1[np.random.randint(1,21,1)]

print(f"random element {r_element}")

index_value = np.where(array_r_1 == r_element)

print(f"index value {index_value}")
array_r_2 =array_r_1.reshape(4,5)
print(array_r_2)

print(array_r_2[:,(1,4)])

array_r_b = np.pad(array_r_2,pad_width=1,mode= 'constant',constant_values=0)
print(f"\n\nafter padding \n\n{array_r_b}")

array_r_3 = np.random.randint(1,100,30)

array_r_3 = array_r_3.reshape(6,5)

print(f"\n\narray_r_3 \n{array_r_3}")


array_r_3.sort()
print(f"\nafter sorting\n{array_r_3}")

np.put(array_r_3,np.random.choice(range(5,6),replace =False),1)

print(f"\nafter replacing random value as 1 \n\n{array_r_3}")

array_5 = np.arange(1,101).reshape(10,10)
print(f"\n\narray_5 \n{array_5}")

print(f"\n[5:]\n{array_5[5:]}")
print(f"\n[4:,5:]\n{array_5[4:,5:]}")
print(f"\n[2:5,4:7]\n{array_5[2:5,4:7]}")
print(f"\n[:,9]\n{array_5[:,9]}")

array_a =((np.random.rand(15)*10).astype(int)).reshape(3,5)
array_b =((np.random.rand(15)*10).astype(int)).reshape(3,5)

print(f"\narray_a\n {array_a}")
print(f"\narray_b\n {array_b}")

print(f"\nsum \n{array_a+array_b}")
print(f"\nproduct \n{array_a*array_b}")
array_division =(array_a/array_b).astype(int)
print(f"\ndivision \n{array_division}")