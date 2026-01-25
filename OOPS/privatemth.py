class account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass          ##(__)means we can set accpass private 

A1=account(1234 ,"abc")
print(A1.accno)
print(A1.__accpass)  ###it will give an error 



