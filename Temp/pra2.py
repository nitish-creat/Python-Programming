import numpy as np
import pandas as pd

s1 = pd.Series()
# print(s1)

l =[1,2,3,4,5,33]
s2 = pd.Series(l)
# print(s2)

s3 = pd.Series([1,2,3], index=['a','b','c'])

# print(s3)


data = {'a':1,'b':2,'c':3}
# s4 = pd.Series(data)
# print(s4)

s5 = pd.Series(data,index=['x','y','z'])
# print(s5)

# print(pd.__version__)

arr = pd.Series(np.arange(11,20))
# print(arr)


a = np.array([])
# print(a.dtype)

a1 = np.array([1,2,4,2,4])
a2 = np.array([4,2,3,2,9])
a3= pd.Series(a1,a2)
a4 = pd.Series([a1,a2])
# print(a3)
# print(a4)


ser1 = pd.Series(np.linspace(3,33,3))
# print(ser1)

ser2 = pd.Series(np.linspace(5,100,30))
# print(ser2)

# print(a1 > a2)


ser3 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

# print(ser3['b'])
# print(ser3[['a','e']])

# print(ser3.loc['a'])

# print(ser3.iloc[4])

# c1 = pd.DataFrame()
# print(c1)

# c2 = pd.DataFrame([1,2,3],columns=['Hellow'])
# print(c2)

# c3 = pd.DataFrame(ser3,columns=['ser3'])
# print(c3)
# c= pd.DataFrame(ser3)
# print(c)
# c4 = pd.DataFrame(c,columns=['c'])
# print(c4)

dataFrame = pd.DataFrame({0:[1,4,7],1:[2,5,8],2:[3,6,9]})

# print(dataFrame)

b1 = pd.Series([1,2,3],index=['A','B','C'])
b2 = pd.Series([4,5,6],index=['B','C','D'])
print(b1+b2)
