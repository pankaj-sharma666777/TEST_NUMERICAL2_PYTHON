import numpy as np
integers =np.array([[1,2,3,4],[5,6,7,135]])
print(integers)

floats =np.array([0.0,0.10,0.12,0.3,0.5,0.63])
print(floats)
print(integers.ndim)
print(floats.ndim)
print(integers.shape)
print(floats.shape)
print(integers.size)
print(floats.size)
for row in integers:
    print(row)

for i in integers.flat:
    print(i)


for i in integers.flat:
    print(i,end="")


print("\n\n")

print(np.zeros(6).reshape(2,3))
print(np.zeros(6))
print(np.ones((3,4),dtype=int))

print(np.full((4,5),14))

print(np.arange(10))
print(np.arange(3,8))
print(np.arange(20,1,-3))
print(np.arange(20,1,-3))
print(np.linspace(0,50))
print(np.linspace(0,6))
print(np.linspace(2,10))
print(np.linspace(0,50,num=5))
print(np.arange(1,31).reshape(5,6))

print(np.random.randint(1,20,6))

rand_array =np.random.randint(1,100,15)
print(rand_array)
print(rand_array.min())
print(rand_array.max())
print(rand_array.sum())
print(rand_array.mean())
print(rand_array.std())

