import numpy as np
array = np.arange(1,11)
print(array)

print(array>5)

print(array[array>5])

condition = array<=4
print(array[condition])

new_condition_1 =(array != 8)& (array>=6)
print(array[new_condition_1])
new_condition_2 =(array<3)^ (array>=6)
print(array[new_condition_2])


