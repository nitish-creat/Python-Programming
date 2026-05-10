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


df_clean = df.dropna()
print("data after dropping missing value : \n",df_clean.head())

df_filled = df.fillna(0)
print("data after filling missing values :\n",df_filled.head())

#group by a column and aggregate
grouped_data = df.groupby('day')['total_bill'].sum()
print("total bill by day",grouped_data)

sorted_df= df.sort_values(by='total_bill',ascending=False)
print("Top 5 total bill record: \n",sorted_df.head())

df['total_bill_in_hundreds'] = df['total_bill'].apply(lambda x: x/100)

print("transformed total bill data:\n",
      df[['total_bill','total_bill_in_hundreds']].head(), "\n")