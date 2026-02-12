import pandas as pd

a = pd.Series([2,3,4,5,5])
b = pd.Series([2,3,2,2,2])
print( a*b )
print( a+b )
print( a/b )
print( a-b )


print(a>b)