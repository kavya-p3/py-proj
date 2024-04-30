class Emp:
    def __init__(self):
        self.name = 'kavya'
        self.salary = 1000

    def display(self):
        print('name is {} and salary is {}'.format(self.name, self.salary))


class Random:
    '''@staticmethod'''
    def incrementedsalary(x):
        x.salary = 11800
        x.display()


z=Emp()
Random.incrementedsalary(z)