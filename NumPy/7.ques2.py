import numpy as np

a = np.array([[5,3,2],[4,1,5],[3,2,4]])
b = np.array([[1,2],[3,4],[5,6]])

a1= np.full([3,3],10)

print(a*a1)

print(a@b)
print(a.dot(b))

print(f"Transpose: \n{a.transpose()}")

print(b.shape)
print(b.ndim)
print(a.dtype)