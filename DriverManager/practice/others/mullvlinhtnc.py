class grandFather():
    def __init__(self):
        self.property1 = 500
        super().__init__()

    def display(self):
        print('grand father\'s property ', self.property1)
        super().display()


class Father(grandFather):
    def __init__(self):
        super().__init__()
        self.property = 700

    def display(self):
        print('father property ', self.property)
        super().display()


class Mother():
    def __init__(self):
        self.property3 = 600
        #super().__init__()

    def display(self):
        print('Mother property ', self.property3)


class Son(Father, Mother):
    def __init__(self):
        print('in son')
        super().__init__()



s = Son()
s.display()
