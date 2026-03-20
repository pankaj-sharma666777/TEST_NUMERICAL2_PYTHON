import numpy as np
coefficient = np.array([[2,1],[-3,6]])
print(coefficient)
output = np.array([5,0])
print(np.linalg.solve(coefficient,output))