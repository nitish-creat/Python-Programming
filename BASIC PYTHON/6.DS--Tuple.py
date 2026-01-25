"""  
A tuple is:
-> Ordered
-> Immutable (this is the key)
-> Can store multiple values
-> Faster & safer than lists

comma create a tuple not parenthesis
 tuples do not have append(), pop(), or remove() methods because tuples are immutable
"""

tup=(1,2,4,5,4)
tup1= 1,3,4,2   # store without parenthesis also
print(tup[:])
print("<<--tuple second -->")
print(tup1[:]) 


tup2 = (2)   ## <-- THIS IS NOT A TUPLE -->
tup3=(2,)   ## <-- this one is tuple -->

# print(tup2[:])  give an error
print("<<-- tuple third -->>")
print(tup3[:])

"""  
else all are the same as list but 
tuple is immutable we can not change that's why it is safe

"""

#  TUPLE UNPACKING 

print("<<--tuple unpacking-->>")

t=(2,3)
a,b = t
print(a) # 2
print(b) # 3

# Swapping also possible through this

a = 5
b = 2
print("\n<<--before swapping-->>")
print(a)
print(b)
a,b=b,a
print("<<--after swapping-->>")
print(a)
print(b)

'''
| Feature | List   | Tuple    |
| ------- | ------ | -------- |
| Mutable | ✅ Yes  | ❌ No     |
| Syntax  | `[ ]`  | `( )`    |
| Methods | Many   | Very few |
| Speed   | Slower | Faster   |
| Safety  | Low    | High     |

'''