import numpy as np

arr2d = np.arange(1,13).reshape(3,4)
print(arr2d)

copyArr = arr2d    # In this memory add will be the same 
# print(id(arr2d))
# print(id(copyArr))

print(copyArr)    # this will also the shallow copy

print(arr2d is copyArr)

'''
shallow copy -> this will achieve when we use view like 
c = a.view()
-> if we make changes in one array then it will reflect to another array also
-> memory add for both will be diff


deep copy -> this will achieve when we use copy like
c= a.copy()
-> if we make change in one array then it will not reflect to another array
-> memory add for both will be diff

'''

print("<<-- shallow copy -->>")
c = arr2d.view()
# print(id(c))
# print(id(arr2d))

c[0][0]=20
print(arr2d)


print("<<-- deep copy -->>")

d = copyArr.copy()
print(d)
