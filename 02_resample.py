import numpy as np
numbers_1 = np.arange(1,10,2)
numbers_rand =np.random.randint(1,20,5)
print(numbers_1)
print(numbers_rand)
print(numbers_1+numbers_rand)
print(numbers_1*numbers_rand)
print(numbers_1/3)
print(numbers_rand/3)
numbers_1 += 5
print(numbers_1)

numbers_rand += 3

print(numbers_rand)