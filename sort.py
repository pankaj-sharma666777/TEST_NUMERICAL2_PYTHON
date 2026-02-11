import numpy as np
variable = np.array([3,5,1,8,6,2,9])

print(variable)
sorted_variable =np.sort(variable)
print(sorted_variable)
print(variable)

example = np.random.normal(30,10,(4,4))
print(example)
example_sorted_vertically = np.sort(example,axis=0)
print(example_sorted_vertically)
example_sorted_horizontally = np.sort(example,axis=1)
print(example_sorted_horizontally)
print(example)

