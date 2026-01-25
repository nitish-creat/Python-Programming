# def squares(x):
#     return x**2
# # list1=[1,2,3,4,5]
# list1= list(map(int,input().split(",")))
# new=list(map(squares,list1))
# print(list(new))

# quo= lambda x:x%2==0
# def fun(x):
#     return x%2==0
# a=list(map(int,input().split(",")))
# l=list(filter(fun,a))


# def new_func():
#     force=lambda x,y:x*y
#     x=int(input())
#     y=int(input())
#     r= f"{force:.2f}"
#     print(r)
#     return force

# force = new_func()

# def force(x,y):
#     z=x*y
#     return f"{z:.2f}"

# x=int(input())
# y=int(input())
# print(force(x,y))


# str1='''"hello adityya
# how are you"'''
# print(str1)
# str2=input("")
# print(str1+str2)


# s1={1,2,3,4,5,6}
# s2={2,4,6,7}
# s3={2,6,7,8}
# print((s1 & s2 & s3))


# def list1():
#     return list(list1)
# l=input()
# print(list1())

# a=int(input())
# b=str(a)
# p=1
# for i in b:
#     p*=int(i)
    
# print(p)
  
    

# def squ(a):
#     c=a**2
#     return c
# b=int(input())
# print(squ(b))


# list1=list(map(int,input("data: ").split(",")))
# r=[]
# for i in range(len(list1)):
#      r.append(int(list1[i]-i))
# print(r)
    

# def pro(n):
#      if n>1:
#           return (n%10)*pro(n//10)
#      else:
#           return 1

# n=int(input())
# print(pro(n))

def gcd(a,b):
     if b==0:
          return a
     else:
          return gcd(b,a%b)
def lcm(a,b):
     return (a*b//gcd(a,b))
a=int(input())
b=int(input())
print(lcm(a,b))