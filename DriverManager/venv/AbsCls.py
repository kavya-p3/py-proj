from abc import *

class Car(ABC):
    def __init__(self,reg):
        self.rego=reg

    def printRego(self):
        print('the rego number is',self.rego)

    @abstractmethod
    def calculate(self,x):
        pass

    @abstractmethod
    def carname(self):
        pass

c=Car('kkk')