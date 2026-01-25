class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True        #absraction== hiding the implementation details of a cass and only showing the essential features to the user
        self.acc=True
        print("car started")

car1=car()
car1.start()

