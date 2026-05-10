import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

arr1 = np.arange(12).reshape(3,4)
# print(arr)

arr1.shape = (4,3)
# print(arr)

mat = np.matrix('1 2 3 ; 4 5 6')


arr3 = np.arange(30).reshape(5,3,2)
# print(arr3)

identity = np.eye(5,5,dtype=int)
# print(identity)

Zero = np.zeros([3,3])
# print(Zero)

ones = np.ones([3,4])
# print(ones)

empty= np.empty([3,5])
# print(empty)


# print(arr3.ndim)

# print(arr3.size)

# print(arr3.shape)


mat1 = np.arange(10).reshape(5,2)
# print("<--- matrix 1 --->>")

# print(mat1)

mat2 = np.arange(10).reshape(2,5)
print("<--- matrix 2 --->")
# print(mat2)

# print(mat1@mat2)

# print(mat1.dot(mat2))

# print(mat1[4,1])    # indexing 

# print(mat2[0:2,1:4]) # slicing

# print(mat1[-1: ,-1:])    # slicing
# print(mat1[-1][-1])   # indexing twice

# print(mat2[-1,-1])

mat3 = np.arange(1,21).reshape(5,4)
# print(mat3)

# print(mat3.cumsum(axis=0))   # column wise
# print(mat3.cumsum(axis=1))   # row wise

a = np.array([1,4,3,4,3,24,2,3,4,3])

# print(np.sort(a))


# print(mat1.flatten())

# print(mat2.T)


arr3 = np.arange(1,10).reshape(3,3)
print("<-- matrix 3 -->\n",arr3)
print(arr3[1:,1:])
print(arr3[:,0])
print(arr3.max(axis=1))

print(arr3.flatten().shape)

print(id(mat3))