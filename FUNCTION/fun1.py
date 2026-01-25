#funtion is used for reduce the line of code 
def calmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if (a>b):
        print("first no. is greater")
    else:
        print("second no. is greater or equal")

a=int(input())
b=int(input())
isgreater(a,b)
calmean(a,b)
c=29
d=30
isgreater(c,d)
calmean(c,d)