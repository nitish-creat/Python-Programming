""" 
A list is:
-> Ordered
-> Mutable (changeable)
-> Can store multiple values
-> Can store different data types

"""


data = [1,3.5,'raman',True]
for i in data:
    print(f"value : {i} and data type : {type(i)}")


print(data[3])

data[3] = False   # Mutable

print(data[3])
print(data[-1])   # start from the end


# Slicing 
# list[start : end]

print(data[1:3])


# APPEND (add at end) Adds only one element at a time

data.append("Hello world")
data.append(1)

print(data[:])

"""
remove() — remove by VALUE
## Removes first occurrence only
<<-- Error if value not present -->>
"""
data.remove(1)
print(data[:])  

""" 
POP() remove by indexing
"""
arr = [1, 2, 3, 4]
arr.pop()   # remove last element
print(arr[:])
#<<-- remove by index -->>
arr.pop(2)
print(arr[:])



# traveral

print("\n<<--- traversal of the array --->>")

list1 = [2,4,1,242,23,2,3,2]

for i in range(len(list1)):
    if list1[i]%2==0:
        print(f"{list1[i]} at position {i}")
    
print("<<-- second method -->>")

for i in list1:
    if i%2==0:
        print(i)   ## Same output