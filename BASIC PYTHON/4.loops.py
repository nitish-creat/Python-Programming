# FOR LOOP
"""
1. for variable in sequence:
    statement                   basic syntax of for loop

    
2. range(start, end, step)

3.when to use for or while loop

| Situation                | Use     |
| ------------------------ | ------- |
| Fixed number of times    | `for`   |
| Looping over list/string | `for`   |
| Condition-based loop     | `while` |
| User input until valid   | `while` |

"""
# FOR LOOP
for i in range(5):
    print(i)

print("<<--second method-->>")
for i in range(1,5):
    print(i)

print("<<--third method-->>")

for i in range(1,11,2):
    print(i)

print("<<--Loop over list-->>")

# LOOP OVER A LIST 
numbers = [1,2,3,4,4]
for i in numbers:
    print(i)


print("<<--loop over string-->>")

name = 'karan'
for ch in name:
    print(ch)

# <<---- WHILE LOOP --->>
""" 
It depend on the condition

while condition:
    statement

"""

print("<<---while Loop Starting --->>")


i =1
while i<=5:
    print(i)
    i+=1

print("<<---second method --->>")

i=0
while True:
    if(i == 5):
        break
    print(i)
    i+=1


print("<<-- third pattern -->>")

print("Enter (0) for exit")
while True:
    choice = int(input("Enter an number : "))
    if(choice == 0):
        print("<---exit--->")
        break
    print("char you enter: ")
    print(choice)
    print("enter again: ")

print("\n<<--fourth concept-->>")

i=1
for i in range(5):
    if i == 2:
        continue
    print(i)
