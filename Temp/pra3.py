import pandas as pd
import numpy as np
df = pd.read_csv("FakeData.csv")
print(df.info)

# print(df.describe())
# print(df.head(2))
# print(df.tail())

# print(df.isnull())
print(df.isnull().sum())


# print(df.dropna())
# print(df.dropna(axis=1))

f_m = df.fillna({
    'Age' : df['Age'].mean(),
    'City' : 'Benaam shehar',
    'Salary' : df['Salary'].median()
})

print(f_m)

for_fill = df.ffill()
# print(for_fill)


back_fill = df.bfill()
# print(back_fill)

df_num = df.select_dtypes(include=[np.number])
df_cat = df.select_dtypes(exclude=np.number)
df_inter = df_num.interpolate()
df_fill = df_cat.ffill()

# df_final = df.copy()

df_final = pd.concat([df_inter,df_fill],axis=1)
df_final = df_final[df.columns]
print(df_final)
# df_final.to_csv("FakeData.csv", index=False) 

grouped_data = df_final.groupby('Name')['Salary'].sum()
print(grouped_data)

sorted_df = df_final.sort_values(by='Salary',ascending=False)
print(sorted_df)

df_final['Total_salary_in_dollar'] = df_final['Salary'].apply(lambda x:x/92)

print(df_final)

