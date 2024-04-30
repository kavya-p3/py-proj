def Bonus (sal):
    def bonus():
        temp=sal()
        return temp+200
    return bonus

def Increment(sal1):
    def increment():
        temp=sal1()
        return temp*1.10
    return increment


def salary ():
    return 10000

gross=Bonus(Increment(salary))
print(gross())