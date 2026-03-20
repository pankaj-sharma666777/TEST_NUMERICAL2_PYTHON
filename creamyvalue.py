import numpy as np


marks = np.array([55, 80, 72, 90, 60])
print("marks")
print(marks)

top3 = np.argpartition(marks, -3)[-3:]
print("top 3 marks")

print(marks[top3])


arr = np.array([10, 4, 7, 2, 8])

indices = np.argpartition(arr, 2)

print(indices)
print(arr[indices])

# Important Rule

# For Top K values

# np.argpartition(arr, -k)[-k:]

# For Smallest K values

# np.argpartition(arr, k)[:k]