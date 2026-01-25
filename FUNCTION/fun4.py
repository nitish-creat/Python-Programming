# def cube(x):
#     return x*3
# l=[1,2,3,4,8]
# newl=[]
# for i in l:
#     newl.append(cube(i))
# print(newl)


cube= lambda x:x**3
filter_fun=lambda a:a>4
# def cube(x):
#     return x*3
l=[1,3,5,6,8,9]
new=list(map(cube,l))   #mapping 
newl=list(filter(filter_fun,l))    #filter
print(newl)
print(new)

#reduce
from functools import reduce
num=[2,4,3,5,6,76,4,5,6,252]
sum=reduce(lambda x,y:x+y,num)
print(sum)
