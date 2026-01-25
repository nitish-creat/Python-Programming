class car:
    @staticmethod
    def start():
        print("car get started")
    @staticmethod
    def stop():
        print("car get stoped")

class toyota(car):
    def __init__(self,name):
        self.n=name

car1=toyota("BMW")
print(car1.n)
print(car1.start())




