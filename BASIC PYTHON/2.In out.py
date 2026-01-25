# input always return the string
#Even if you type 20, Python sees "20".

age=int(input("Enter your age: "))
print(type(age))   # string
print(age) # "age"

# print(age+5)  # Error becuse of the type is string

# str + int = illegal


print("<---Second part--->\n")

value = int(input('Enter your value: '))

print(value + 10);


print("<--Thrid Part-->\n")
print("F-strings\n")

city="Yamuna Nagar"

print("age:",age,"city:",city)   # this method is good but you can't do calculation here like age+1 so for that we use f strings 

print(f"age is {age+10}, and city is :{city}")
# now this works correctly
# Inside {} you can write any valid Python expression.

print(f"length of the city: {len(city)}")

#Decimal precision

pi = 3.1415926
print(f"value of pi: {pi:.2f}")

#Integer Padding

num= 9

print(f"num after padding: {num:02}") # 09
