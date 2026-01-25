# def append(filename,text):
#     try:
#         with open(filename,'a') as f:
#             f.write(text)

#         with open(filename,'r') as f:
#             data=f.read()
#             print(data)


#     except FileNotFoundError:
#         print("invalid")

# f=input("enter your file name")
# t=input("enter your text")
# append(f,t)

# def checkdata(filename):
#     try:
#         with open(filename,'r') as f:
#             data=f.readlines()

#         sentences=(len(data))
#         words=sum(len(i.split()) for i in data)
#         char=sum(len(i) for i in data)


#         print("sentences",sentences)
#         print("words",words)
#         print("char",char)


#     except FileExistsError:
#         print("invalid")
# filename=input("enter your file name")
# checkdata(filename)

# def count(filename,text):
#     try:
#         c=0
#         with open(filename,'r') as file:

#            for i in file:
#                if i.startswith(text):
#                    c+=1

#         print(c)

#     except FileNotFoundError:
#         print("invalid")

# filename=input()
# t=input()
# count(filename,t)


# a=input()
# b=input()
# try:

#     with open("d.txt",'r') as f:
#         data=f.read()

#         if a in data:
#             print(data.replace(a,b))
#         else:
#             print("invalid")


# except ValueError:
#     print("value is in correct")



# with open("d.txt",'r') as f:
#     data=f.readlines()
#     rev=data[::-1]
#     for i in rev:
#         i=i.strip()
#         print(i)


# with open("d.txt",'r') as f:
#     data=f.read()
#     check=set()

#     for i in data:
#         if i not in check:
#             print(f"{i}={data.count(i)}")
#             check.add(i)



# with open("sample.txt",'a') as f:
#     f.write("hello python")

# with open("sample.txt",'r') as f:
#     data=f.read()

# for i in data:
#     if i == "p":
#         r=(data.replace("p","="))

# print(r)


# def prime(num):
#     if num<2:
#         return "not prime number"

#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return "not prime"

#     return "prime"

# numbers=list(map(int,input().split(',')))
# result={num: prime(num) for num in numbers}
# print(result)



# str1=[4,2,3]

# print(str1[0]**3)
# print(str1[-1]**3)

# print((str1[0]**3)*(str1[-1]**3))

# with open("sample1.txt",'a') as f:
#     f.write("1,2,3,4,5,6,7,8,9")

# with open("sample1.txt",'r') as f:
#     data=f.read()
    
#     for i in data:
#         if i ==",":
#             continue
#         else:

#             result=int(i)*3       
#         print(result, end=' ')
        
# str1=input()
# str2=""

# for i in str1:
#     if i not in str2:
#         print(f"{i}:{str1.count(i)}")
#         str2+=i


with open("d.txt",'r') as f:
    data=f.readlines()
    for i in data:
        print(i.capitalize())

