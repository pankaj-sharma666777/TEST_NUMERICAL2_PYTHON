import numpy as np
example = np.arange(10,20)
print(example)
print(f"from[2:6]{example[2:6]}")
print(f"[3::2]{example[3::2]}")
print(f"[:7:3]{example[:7:3]}")

array = np.arange(30).reshape(6,5)
print("\n\n")
print(array)
print("\n\n")

print(array[2,:])
print("\n\n")

print(array[2])
print("\n\n")

print(array[0])
print("\n\n")

print(array[:,2])
print("\n\n")

print(array[:,0])
print("\n\n")

print(array[1:4,0:3])
print(array[0::2,0::2])
print(array[1:4,0:3])
print(array[1:4,0:3])



