import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Rainfall.csv")

print(df.info)

print(df.isnull().sum())

# print(df.isnull().sum() / len(df)) * 100

df_drop = df.dropna()
print(df.shape)
print(df_drop.shape)

print(df['Annual'].mean())
print(df['Annual'].median())
print(df['Annual'].std())


region_avg = df.groupby('Subdivision')['Annual'].mean()

print(region_avg.sort_values)

# yearly_avg = df.groupby('Year')['Annual'].mean()

# plt.figure(figsize=(10,5))
# plt.plot(yearly_avg)
# plt.title("Yearly Average")
# plt.show()

print(df['Annual'].sum())


df_mean = df.fillna(df.mean(numeric_only=True))
print(df_mean)


seasonal_avg = df[['APR','AUG','DEC','FEB','JAN','JUL','JUN']]

seasonal_avg.plot(kind='hist')
plt.title("Sealsonaly avg")
plt.show()