'''
Library → a collection of code that provides functionality
Package → a structured container that organizes libraries/modules
'''

import numpy as np

a = np.arange(1,5).reshape(2,2)
print("<<-- arange using reshape -->>")
print(a)

zero = np.zeros([3,3],dtype=int)
print(zero)

val =  np.random.randint(1,100,size=(3,3))
print(val)

b = np.matrix('2 3 4 , 5 6 7, 9 10 11')


print("<<-- array operations -->>")

print(np.sum(a))


'''
print(a@b)
print(a.dot(b))  m x n and n x z  

'''


# element by element cal

print(a*2)
print(a**2)

# matrix multiplication 
# print(zero @ b)
# print(a.dot(b))
