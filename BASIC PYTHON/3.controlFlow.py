"""
1.
| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | equal to         |
| `!=`     | not equal        |
| `>`      | greater than     |
| `<`      | less than        |
| `>=`     | greater or equal |
| `<=`     | less or equal    |


2. Python uses indentation
"""

age=-10

if age <= 0:
    print("Invalid age.. :)")
elif age>=18:
    print("Eligible for the vote")
elif age < 18:
    print("not eligible for the vote")


a = 10
b =1 
print(a == b)
print(a > b)

""" <-- logical operator -->"""

# AND 

marks =90

if marks<=100 and marks>=90:
    print("O grade")
elif marks>=70 and marks<90:
    print("A+ grade")

# OR

marks = 35

if marks >= 40 or marks == 35:
    print("Pass by grace")


#NOT
logged_in = False

if not logged_in:
    print("Please login first")



username = input("Enter username: ")
password = input("Enter pass: ")

if username == 'hello' and password == '123':
    print("Login successfully")
else:
    print("Invalid credentials")