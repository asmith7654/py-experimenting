import numpy as np

list1 = [0,1,2]
array1 = np.array(list1)
array2 = np.zeros((2,3))
array3 = np.arange(0,11)
array4 = np.random.randint(1, 24, size=(2,3,4))
array5 = np.random.rand(100, 2)

matrix1 = np.arange(1,10)
matrix1 = matrix1.reshape(3,3)

matrix2 = np.random.randint(0,2,size=(3,3))

matrix3 = matrix1 * matrix2

matrix4 = matrix1.T

matrix5 = matrix1 @ matrix1

print(matrix5)
# print(array4[0,0:2,0:2])
# print(array4.sum())
# print(array4.mean())
# print(array4.std())
# print(array4.var())
# print(array4.max())
# print(array4.min())