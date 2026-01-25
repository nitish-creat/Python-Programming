class student:
    def __init__(self,name):
        self.n=name
    def getname(self):
        return self.n
s1=student("nitish rana")
print(s1.n)
print(s1.getname())
del s1
print(s1.getname())          ##IT WAS DELETED BY THE PROGRAM