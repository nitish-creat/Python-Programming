# print(1+2)# adding
# print("nitish"+"rana")#concatenate
# print([1,2,3,4]+[2,5,3])#merge
# ##different meaning of adding


class complex:
    def __init__(self,real,img):
        self.R=real
        self.I=img
    def number(self):
        print(self.R,"i +",self.I,"j")

num1=complex(1,2)
num1.number()


