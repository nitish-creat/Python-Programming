import pandas as pd 
import numpy as np

arr = pd.Series([[1,2,3,4],[4,33,3,4]])
print(arr)

a = pd.Series(np.arange(1,6))
print(a)

mul = pd.Series([[2,32,3],['a']])
print(mul)
ser1= pd.Series(np.linspace(3,33,3))
# linspace(3,33,3)  start, space, element no.
 

# print(mul.iloc[1])
# print(mul[1])

print(ser1)

ser2 = pd.Series([2,3,4,3], name="nothing", index=[2,4,5,6])
print(ser2)

ser3= pd.Series(np.arange(6),index=['a','b','c','d','e','f'])

print(ser3)
print('b' in ser3)
print('b3' in ser3)
print('c' in ser3)

