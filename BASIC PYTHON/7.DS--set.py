'''  
A set is:
-> Unordered
-> ** Stores unique elements only **
-> Mutable (you can add/remove items)
-> Very fast for membership checking

-> duplicate element are remove automatically and give sorted array
->You cannot put a list inside a set
'''

s={1,2,2,31,1,41,2,3}
print(s)

# s={}  this is dic not set 

# s = set() this one is set 

# print(s[0]) #this will fail

s.add(20)
print(s)

s.remove(20)   # but when element is not found in set it will give error so that's why we se discard instead of remove
print(s)

s.discard(12)  # this will not give an error
print(s)
s.pop()   # remove the random element
print(s)
s.clear()
print(s)


s1 = {2,4,1}
s2 = {3,1,2}

print(s1 | s2)  # UNION
print(s1 & s2)  # INTERSECTION 
print(s1 - s2)

print(s1 ^ s2)  


print(2 in s1)

'''
| Feature  | List | Tuple | Set |
| -------- | ---- | ----- | --- |
| Ordered  | ✅    | ✅     | ❌   |
| Unique   | ❌    | ❌     | ✅   |
| Mutable  | ✅    | ❌     | ✅   |
| Indexing | ✅    | ✅     | ❌   |

'''