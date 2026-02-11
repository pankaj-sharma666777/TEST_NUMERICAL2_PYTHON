import numpy as np
array = np.arange(20).reshape(5,4)
print(array)
print(np.split(array,[1,3]))
x,y,z = np.split(array,[1,3])
print(x)
print(y)
print(z)
s,t,u =np.split(array,[1,3],axis=1)
print(s)
print(t)
print(u)

# hsplit function
print("\nhsplit\n")
print(np.hsplit(array,4))

print("\nhsplitunequal\n")
print(np.hsplit(array,[1,3]))
#vsplit function
print(array)
print(np.vsplit(array,5))
print("\n\n")
print(np.vsplit(array,[2,4]))


