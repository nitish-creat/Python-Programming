import pandas as pd
'''
s.index      # returns index
s.values     # returns values
s.dtype      # data type
s.shape      # size in tuple
s.size       # total elements
s.ndim       # dimension (always 1)
'''
lst = [1,2,33,4,3,5]
print(lst)

'''
IT ALSO PRINT THE INDEX AND THEN ITS VALUE IN COLUMN 
'''

series = pd.Series(lst)
print(series)   # IN THIS DATA TYPE WILL BE INT64

empty = pd.Series([1])
print(empty)    # IN THIS DATA TYPE WILL BE OBJECT

# CUSTOM INDEX 

arr = pd.Series(['p','q','r',1] , index = [10,20,30,40])
print(arr)  # now the data type will be object

arr1 = pd.Series([1,2,3,4,5] , name="nothing")
print(arr1)    # now the name of the arr1 is nothing

scalar_series = pd.Series(0.5,index=[1,2,3])
print(scalar_series)
'''
output will be
1    0.5
2    0.5
3    0.5
'''

dic ={'a':20,'b':10}
dicSer = pd.Series(dic)
print(dicSer)

print(dicSer.index)


