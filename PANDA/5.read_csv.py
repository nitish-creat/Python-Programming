'''
DATA COLLECTION  
    -> READ CSV
    -> READ EXCEL
PRE PROCESSING
    ->INFO()      PANDAS
    ->DESCIBE()     PANDAS
MODEL
    ->
EVALUATION
    ->
VISUAL / O P
    ->
'''



import pandas as pd

a = pd.read_csv('ABC.csv')
# print(a)
# print("<<<--Info-->>")
# print(a.info())
# print("<<--descibe-->>")
# print(a.describe())


b = pd.read_excel('Fake.xlsx')
print("<<-- Excel file -->>")
# print(b.info())
# print(b.describe())

print(b.head())
# print(b.shape())
