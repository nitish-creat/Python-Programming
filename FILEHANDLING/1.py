# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# # line1=f.readline()
# # print(line1)
# # line2=f.readline()
# # print(line2)
f=open("demo.txt","w")
f.write("hlo this the new line")
data=f.write("hello nahi")
f.close()




#writing and append

# f=open("demo.txt","w")
# f.write("I want to learn javascript")
# f.close()

# f=open("demo.txt","a")
# f.write("\nbut I want to learn pyhton first")


#write and append mode mein agr file exist ni krti to python khud ek file create krr deta hai 

# f=open("sample.txt","w")               ##file apne app create hogyi
# f.write("this is your new file created by the python")
# f.close()