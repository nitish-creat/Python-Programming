import numpy as np

n = int(input("Enter your number: "))
l=[]

for i in range(0,n):
    l.append(int(input(f"Enter the {i+1} value : ")))

arr = np.array(l)

print(arr)

avg = np.average(arr)
print(f"Average of this: {avg}")

if avg>=90 and avg<100:
    print("A")
elif avg>=80 and avg<90:
    print("B")
elif avg>=70 and avg<80:
    print("C")
else:
    print("D")