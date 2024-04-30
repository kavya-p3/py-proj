class myclass:
    def __init__(self):
        self.name = 'kavya'
        self.__age = 30
    def display(self):
        print(self.name , self.__age)

class baby(myclass):
    def babydisplay(self):
        print(self.name)


v = myclass()

print(_myclass.__age)