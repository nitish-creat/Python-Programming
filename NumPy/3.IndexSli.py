import numpy as np

# a1=np.array([[1,9,42,],[3,2,5]])
# print(a1[-2][-2])   # row and col    Indexing

# print(a1[0:,1:])   # Slicing 

# print(a1[1][1])
# print(a1[0:1][0:1])

# print(a1[1:2][0:1])

# print(a1[1:2][1:1])

# a2=np.arange(12).reshape(3,4)
# print(a2[0:3,0:2])
# # print(a2[-2:-1,-3:-1])

# print("\n")

# print(a2[1:2,1:3])

# print("\n")
# b = np.matrix('1 2 3 4 , 5 6 7 8')
# print(b[0:1,0:2])

# print(b[0][1])    indexing will not work on matrix


'''
FUCNTION USIGN NUMPY
'''

arr = np.array([1,2,4,2,42,4,2,1344,2,2343,32])
print(f"sorted array: {np.sort(arr)}")
print(f"sum of the array: {np.sum(arr)}")
print(f"max of the array: {np.max(arr)}")
print(f"min of the array: {np.min(arr)}")

arr2= np.arange(12).reshape(3,4)

print(f"\nmain array : \n {arr2}")
print(f"\nCummulative sum column wise :\n {arr2.cumsum(axis=0)}")

print(f"\nCummulative sum row wise :\n {arr2.cumsum(axis=1)}")

print(f"\nconvert the 2d array in 1d using flatten: {arr2.flatten()}")

print(f"\ntranspose function :\n {arr2.transpose()}\n")

print(f"the sum of the column wise: {arr2.sum(axis=1)}")