class Aa:
    def __init__(self,p=0):
        '''self.pro=p
        self.ty='kkk' '''
        pass


    def printF(self):
        print('the prop value',self.property)

    def __mod__(self, other):
        return self.prop%other.prop

    def __ne__(self, other):
        return self.prop !=other.prop
    def __pow__(self,others):
        return self.prop**others.prop

class Bb(Aa):
    '''def __init__(self,p=1):
        self.prop=p
        self.zz='zz'''

    def __add__(self, other):
        return self.prop+other.prop
    def display(self):
        self.prop=5
        print('sub - const',self.prop)
        print('parent const',self.pro)

b=Bb(2)
b.display()


