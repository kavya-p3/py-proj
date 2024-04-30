class Test:
    def __init__(self):
        self.x=10

    def mutate(self):
        self.x=20

    def checkOnX(self):
        print("check on fnc",self.x)


s1=Test()
print('s1 value ',s1.x)
s1.mutate()
print('after mutation',s1.x)
print('s1 value ',s1.x)
s1.x=40
s1.checkOnX()
