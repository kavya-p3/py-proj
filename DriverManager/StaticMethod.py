class Emp():
    glob=0
    def __init__(self,n,i,s):
        self.name=n
        self.id=i
        self.salary=s

    def display(self):
        print('inside emp')
        print('the name is {} and id is {} with salary {} and manager {}'.format(self.name,self.id,self.salary,self.manager))


class Temp():
    @staticmethod
    def change(Emp.glob):
        t.salary=98
        t.manager='kevin'
        t.display()

e=Emp('kavya',123,55)
Temp.change(Emp.glob)
e.display()
