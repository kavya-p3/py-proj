class A:
    b = 100
    #@classmethod
    def display():
        print(cls.b)


c = A()
c.display()