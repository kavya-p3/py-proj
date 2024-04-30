from AbsCls import Car

class Santro(Car):
    def __init__(self,x,yr):
        self.y=yr
        super().__init__(x)
    def calculate(self,x):
        total=self.y+x
        print('the total is ',total)
    def print(self):
        print("in print method")

    def carname(self):
        pass

s=Santro('reg:xx',100)
s.printRego()
s.calculate(3)
s.print()
