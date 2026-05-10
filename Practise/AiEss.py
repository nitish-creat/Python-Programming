import numpy as np

# print("<-- Dot Product -->")
# x = np.array([3,2])
# y = np.array([5,4])

# dot_pro = np.dot(x,y)
# print(dot_pro)

# mat1 = np.arange(4).reshape(2,2)
# mat2 = np.arange(4,8).reshape(2,2)
# print(mat1)
# print(mat2)
# print("<-- multiplication of matrix-->>")
# print(mat1@mat2)
# print("<-- Addition of matrix-->>")

# print(mat1+mat2)

# print("<<--Transpose of matrix-->>")
# print(mat1.T)


# print("<-- solve linear equations -->")

# #2x +y = 5
# # x+y = 3

# a = np.array([[2,1],[1,1]])
# b = np.array([5,3])
# solution = np.linalg.solve(a,b)
# print(solution)


# A = np. array([[3,2],[1,4]])
# print(A)

# print("<-- determinant -->")

# det = np.linalg.det(A)
# print(f"{det:.2f}")

# print("<-- inverse -->")

# inv = np.linalg.inv(A)
# print(inv)

# B =1
# prediction = np.dot(x,y)+B
# print("<-- prediction -->")
# print(prediction)

m = np.arange(1,10).reshape(3,3)
print(m)
n = np.arange(11,20).reshape(3,3)
print(n)

print("determinant",np.linalg.det(m))



