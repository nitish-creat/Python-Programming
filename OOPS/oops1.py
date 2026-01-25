####NONSTATIC MTH****
###Encapsulation==wraping data and functions into a single unit (object) ***

# class student:              #creating class
#     name="nitish rana"      
#     name2="nikhil"

# s1=student()            #creating object
# print(s1.name)
# s2=student() 
# print(s2.name2)




# class car:
#     brand="BMW"
#     color="black"

# car1=car()
# print(car1.brand)
# print(car1.color)




# class student:
#     name="ram"        #class attribute
#     def __init__(self,fullname,marks):           ####constructor####
#         self.name=fullname            #object attribute        #obj attr>class attr
#         self.marks=marks
#         print("adding a new student...")
    
#     def welcome(self):
#         print("welcome student",self.name)               #self likhna padega vrna error aajayeg   


# s1=student("nitish rana",98)
# s1.welcome()
# print(s1.name,"and his marks",s1.marks)

# s2=student("nikhil",99)
# s2.welcome()
# print(s2.name ,"and his marks",s2.marks)


class student:
    def __init__(self,Name,Sname,Smarks):
        self.Name=Name
        self.name=Sname
        self.marks=Smarks
        print("here is the result of the student") 
    
    def result(self):
        print("the name of the student is:",self.Name)
        print("suject name:",self.name)
        print("the marks of the student in phy,chem,math is :",self.marks)

    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("the avg of his marks is:",sum/3)

    @staticmethod       #static method
    def last():
        print("I hope you are satisfy with your numbers..")

s1=student("nitish rana",["phy","chem","math"],[95,93,96])
s1.result()
s1.get_avg()
s1.last()




