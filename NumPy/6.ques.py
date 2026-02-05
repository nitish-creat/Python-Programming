import numpy as np

row = int(input("enter the row no. : "))
col = int(input("enter the col no. "))
n = row*col

l=[]

for i in range(0,n):
    l.append(int(input(f"enter the {i} element : ")))

a =np.array(l)
a.shape = (row,col)

print(a)
print(f"Max : {a.max(axis=0)}")    # Max col wise
print(f"Min : {a.min(axis=1)}")  # Min row wise
print(f"Total : {np.sum(a)}")  

print(f"cummulative sum column wise : {a.cumsum(axis=0)}")

print(f"convert 2d to 1d array: {a.flatten()}")

print(f"Trasform col to row and row to col: \n{a.reshape(col,row)}")