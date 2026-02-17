'''
NUMERICAL
-> FUNCTION -> INTERPOLATE()
    -> CONTINOUS  (MEAN)
        -> LIKE ( 25 -> 30 )
                (20 - 25 )
    -> DISCRETE  (PINCODE) ,( MEDIAN )
        ->LIKE  (30 , 39)
CATEGORICAL   (MODE)
-> FUCNTION -> FFILL() (FORWARD FILL), BFILL() (BACKWARD FILL)
    -> NOMINAL 
        -> RANDOM ORDER
    -> ORDINAL
        -> ORDERED

'''
import pandas as pd
import numpy as np

data = {
    'id' : [1,2,3,4,5],
    'Name' : ['Sarvesh','Nayanava',np.nan,'harman','Eve'],
    'Age' : [19,np.nan,20,np.nan,90],
    'City' : ['Haryana','West Bengal',np.nan,'panipat','New York'],
    'Salary' :[5000000,53000,204004,np.nan,403020] 
}

df = pd.DataFrame(data)

print(df)


''' 
-> Detecting missing value
'''
print("Missing value in each column")
print(df.isnull().sum())

# df['Name'] = df['Name'].fillna('Be Naam')
# df['City'] = df['City'].fillna('GumShuda')

# print(df)

df_filled = df.fillna({'Age':df['Age'].mean(),
                       'Salary':df['Salary'].median(),
                       'City' : 'Gumshuda',
                       'Name' : "be naam"
                       })


print(df_filled)

# Dropping rows with missing values

df_dropped_rows = df.dropna()
print("<<-- Dropping rows with missing value -->>")
print(df_dropped_rows)

df_dropped_col = df.dropna(axis=1)
print("<<-- Dropping cols with missing value -->>")
print(df_dropped_col)

