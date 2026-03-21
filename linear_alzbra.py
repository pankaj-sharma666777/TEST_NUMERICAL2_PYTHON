import numpy as np
vector_1 =np.array([1,2,3,4,5,6,7,8,9,10])
print(f"vector_1\n{vector_1}")
print(f"vector_1*2\n{vector_1*2}")
print(f"vector_1+5\n{vector_1+5}")

vector_2 = np.array([2,1,3,4,5,7,8,6,10,9])

print(f"vector_2\n{vector_2}")
print(f"vector_1+vector_2\n{vector_1+vector_2}\n")

matrix_1 =np.random.randint(50,size=(5,5))

print(f"\n{matrix_1}")
print(f"\n{matrix_1+5}")
print(f"\n{matrix_1*3}")

tensor_1 =np.random.randint(50,size=(3,3,5))
print(tensor_1)

print(vector_1.shape)
print(matrix_1.shape)
print(tensor_1.shape)


print(vector_1.size)
print(matrix_1.size)
print(tensor_1.size)

vector_1.dot(vector_2)
matrix_a = np.random.randint(10,size=(2,2))

print(f"\n matrix_a \n {matrix_a}")

matrix_b = np.random.randint(10,size=(2,2))
print(f"\nmatrix_b \n{matrix_b}")

print(f"\n 1st element \n{matrix_a[0,0]}")
print(f"\n1st column of matrix_a element \n{matrix_a[:,0]}")

matix_prod =matrix_a.dot(matrix_b)

print(f"\n mulplication\n {matix_prod}")
print(f"\nmatrix_a\n {matrix_a}")
print(f"\nmatrix_b\n {matrix_b}")

print(f"\nidentity matrix order 4\n {np.identity(4)}")

matrix_d = np.random.randint(10,size=(4,4))

print(f"\nmatrix_d\n{matrix_d}")
print(f"\nwhen multiplied with \nidentity matrix of\norder 4\n{np.dot(matrix_d,np.identity(4))}")

matrix_e = np.linalg.inv(matrix_d)

print(f"\nmatrix_e\n{matrix_e}")

print(f"dot(\nmatrix_d,matrix_e\n{np.dot(matrix_d,matrix_e)}")

matrix_f = np.random.randint(10,size=(3,4))

matrix_g = np.random.randint(10,size=(4,3))
 
print(f"\ndot(matrix_f,matrix_g)\n{np.dot(matrix_f,matrix_g)}")
print(f"\ndot(matrix_g,matrix_f)\n{np.dot(matrix_g,matrix_f)}")

vector_3 = np.random.randint(1,15,4)

print(f"\nvector_3 \n{vector_3}")
print(f"\nvdot of(vector_3,matrix_a) \n{np.vdot(vector_3,matrix_a)}")
print(f"\nmatrix_a \n{matrix_a}")
print(f"\nmatrix_b \n{matrix_b}")
print(f"\nmatmul(matrix_a,matrx_b)\n{np.matmul(matrix_a,matrix_b)}")

matrix_det = np.matrix(np.random.randint(10,size=(2,2)))

print(f"\nmatrix_det is \n{matrix_det}")



print(f"\n determinant is\n{np.linalg.det(matrix_det)}")


