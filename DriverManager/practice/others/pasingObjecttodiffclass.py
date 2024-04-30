class Emp:
    def __init__(self):
        self.name = 'hdfc'
        self.balance = 555

    def displaybal(self):
        print('in Emp',self.balance)
        print(self.name)

class Myclass:
    @staticmethod
    def incrementbal(k):
        k.balance = 999
        k.displaybal()

e = Emp()
e.displaybal()
s = Myclass()
s.incrementbal(e)
e.displaybal()