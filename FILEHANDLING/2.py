with open("2.txt","r") as f:
    data=f.read()
    print(data) 


with open("2.txt","w") as f:
    data=f.write("firstly I want to learn HTML")
    print(data)

with open("2.txt","a") as f:
    data=f.write("\nand then I go css")
    print(data)


with open("hlo.txt","a") as f:
    data=f.write("this file is created and whe we use deleting method it will delete")
    print(data)
    
import os
os.remove("hlo.txt")

