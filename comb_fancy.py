import numpy as np

example =np.arange(1,17).reshape(4,4)
print(example)
example[1,[1,3]]
print(example[1,[1,3]])
example[[0,3],1]
print(example[[0,3],1])