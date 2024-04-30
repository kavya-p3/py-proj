class Sampl:
    x = 10
    def __init__(self):
        self.y = 100

    def displ(self):
        self.x = 101
        self.m = 500
        print('in displ x={}'.format(self.x))

ob1 = Sampl()
ob2 = Sampl()
ob1.displ()
print('ob2 x',ob2.x)
ob3 = Sampl()
print('ob3 x',ob3.x)
print(Sampl.m)

