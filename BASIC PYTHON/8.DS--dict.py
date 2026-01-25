
'''
dict are storing key:value pairs 

->Keys must be unique
->Keys must be immutable
->Keys can be:
    ->int
    ->str
    ->tuple
'''

student ={
    "name":"arman",
    "age":20,
    "city":"saharanpur"
}


print(student["name"])   # this will safe until value is present otherwise it will give an error

print(student.get("name"))   # safest method


d ={}  # empty dic
student["name"] = "malik"
print(student)


del student["age"]  # key must exists 
print(student)

# student.clear()
# print(student)


# LOOP THROUGH VALUES
for value in student.values():
    print(value)

# LOOP THROUGH KEY VALUE PAIR

for key,value in student.items():
    print(key,value)


print("<<--checking purpose-->>")
if "name" in student:
    print("Key exists")
