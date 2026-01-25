class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        print("your toatal balance is:")
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"is debited in your account")
        print("now total balance is",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"is creadit in your account")
        print("now total balance is",self.get_balance())


    def get_balance(self):
        return self.balance




s1=account(5000,1234)
print(s1.balance)
s1.debit(3000)
s1.credit(2000)
s1.debit(453)
s1.credit(342)