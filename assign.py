import numpy as np
variable = np.array([0,1,2,3,7,5,6,9,8,9])
print(variable)
variable[4]=4
variable[7]=7
print(variable)
variable[0:5] =10
print(variable)
print(variable[5:])
variable[5:] = 20,30,40,50,60
print(variable)
#assignig values to 2d arrays
print("\n\n")
example = np.array([[10,20,30],
                    [40,50,60],
                    [70,80,90]])


print(example)
print("100 in place of 50")
example[1,1] = 100
print(example)
print("100.4 in place 40")
example[1,0] = 100.4
print(example)

