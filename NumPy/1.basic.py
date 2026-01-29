import numpy as np
print("<<--- 1D Array --->>")

a = np.array([1,3,5,5,2,])
print(a)
print(f"type of the array : {type(a)}")
print("\n<<--- 2D Array --->>")

b=np.array([[1,2,3,4,5],[9,8,7,6,5]])
print(b)

print("\n<<--- 3D Array --->>")

c =  np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])

print(c)
print(f"size of the array : {c.size}")
print(f"\ndimmmension of array {c.ndim}")
print("\n<-- shape of the array (rows and col) -->>")
print(c.shape)    #it is used to reshape or restructure the array    shape is keyword, not a function 

print(f"data type of the array : {c.dtype}")


'''
Arange --> array range  this is only use for 1d array
but we can convert it into 2d or 3d

reshape will structure our array
'''

print("<-- arange ->")

d= np.arange(1,11,2)
print(d)

# converting arange into 2d array 
reshape= np.arange(15).reshape(3,5)   # no of rows , no of col respectively

print('\n<-- 1d array using arange -->')
print(d)
print('\n<-- 2d array using arange -->')
print(reshape)

'''
matrix is used for 1d or 2d array only 
'''
print("<--matrix-->")
mat=np.matrix('1 2 3 ; 4 5 0')
print(mat)

print(f"value at index 0 and 0 {mat[1][0]}")