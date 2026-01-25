# with open("practise.txt","w") as f:
#     data=f.write("Hlo.my name is arjun\nand i want to learn css\nbut firstly i sholud learn HTML..")
    
# with open("practise.txt","r") as f:
#     data=f.read()

# new=data.replace("HTML","basic of html")
# print(new)
# # new2=data.replace("css","dsa")
# # print(new2)

# with open("practise.txt","w") as f:
#     f.write(new)
#     # f.write(new2)
#     # data1=f.write(new2)


# word="xxxhtml"
# with open("practise.txt","r") as f:
#     data=f.read()
#     if word in data:
#         print("found")
#     else:
#         print("not found")


def checkline():
    word=input()
    data=True
    line=1
    with open("practise.txt","r") as f:
        while data:
            data=f.readline()
            if word in data:
                print(line)
                return
            line+=1

    return "chala ja bsdk"

print(checkline())
