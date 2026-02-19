import pandas as pd

df = pd.read_excel('tips.xlsx')
# print(df)
'''
head -> by default it give the 5 first rows
tail -> by defalut it give the 5 last rows

'''
# display first 10 rows
# print("first 10 rows : ",df.head(10))

#display last 5 rows

# print("last 5 rows : ",df.tail())  # by default it take 5 rows

# print("data frame info: ")
df.info()
# -> structure of this 244 col and 7 rows
#Descriptive statistics 

print("describe statistics: \n",df.describe())
print("Shape of data frame:\n ",df.shape)
print("column names: \n",df.columns)
print("missing values: \n",df.isnull().sum())
