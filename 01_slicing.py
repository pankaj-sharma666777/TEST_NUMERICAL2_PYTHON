import numpy as np
n_array_1 = np.random.randint(1,30,8)
print(n_array_1)
print(n_array_1[3])
print(n_array_1[2:7])
print(n_array_1[:3])

n_array_2 = np.arange(1,7)

print(n_array_2)
n_array_2[:3] = 7

print(n_array_2)

n_array_3 =np.random.randint(1,100,20)

print(n_array_3)
n_array_3 = n_array_3.reshape(5,4)
print(n_array_3)
print(n_array_3[4])
print(n_array_3[3,0])
print(n_array_3[:2])

print(n_array_3[:,2:4])
print(n_array_3[:,(2,3)])

n_array_4 =np.arange(1,7)
print(f"before operation {n_array_4}")

n_array_4_SC =n_array_4.view()   #shallow copy of n_array_4
print(f"shallow copy before operation {n_array_4_SC}")

n_array_4[3]*=7
print(f"after operation {n_array_4}")

print(f"shallow copy {n_array_4_SC}")
 
n_array_4_SC[2] += 5 
print(f"applying operation to shalow copy {n_array_4_SC}")

print(f"original array {n_array_4}")

n_array_4_DC =n_array_4.copy()
print(f"direct copy before opration {n_array_4_DC}")

n_array_4_DC[1] -= 5
print(f"direct copy {n_array_4_DC}")
print(f"original array{n_array_4}")
print(f"shallow copy{n_array_4_SC}")


