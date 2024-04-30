#Python program to print negative numbers in a list
def printAllNeg(lst):
    l = []
    for i in lst:
        if i<0:
            l.append(i)

    return l

lst = [-8,0,0.5,88,-100,-5,-6666,111,-1]
lst2 = printAllNeg(lst)
print(lst2)