import numpy as np
'''
start : stop : step

'''

arr = np.array([1,2,3,4,3,4])

print(arr[1:3])  # 2,3
print(arr[::-1])  # reverse the 
print(arr[::2])  #start from 1 and end to the last with 2 steps


'''
2d array slicing 
-> arr2d[ rows , columns ]

'''

print("\n\n<<-- 2D array -->>")

arr2d = np.arange(1,13).reshape(3,4)
print(arr2d)
print('\n')
print(arr2d[0,:])  #select the 0th index full row

print(arr2d[:,2])

print(arr2d[1,0:2])  # 5,6
print(arr2d[0:2,0:2])


'''
Negative indexing
arr2d[-1, :]     # last row
arr2d[:, -1]     # last column

'''

print(arr2d[-1,:])
print(arr2d[:,-1])