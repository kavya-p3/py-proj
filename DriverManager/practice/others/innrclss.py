class Person:
    def __init__(self):
        self.name = 'kavya'
        self.db = self.DOB()

    def disp(self):
        print(self.name)
        self.db.dispDOB()

    class DOB:
        def __init__(self):
            self.mm = 4
            self.dd = 19
            self.yyyy = 1990
        def dispDOB(self):
            print('{}/{}/{}'.format(self.mm,self.dd,self.yyyy))


p = Person().DOB()
p.dispDOB()