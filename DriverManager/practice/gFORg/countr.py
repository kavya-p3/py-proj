# Python program to demonstrate accessing of 
# Counter elements 
from collections import Counter 

# Create a list 
z1 = ['blue', 'red', 'blue', 'yellow', 'blue', 'red','yellow', 'yellow','yellow']
z2 = ['pink', 'red', 'blue', 'yellow', 'pink', 'red','yellow', 'yellow','yellow']
z = Counter(z1)
ls =[1,2,3,4,4]
st = 'kavya'
di = {'marron':5}

z.update(ls)
z.update(di)
z.update(st)


c = Counter(a=3, b=1,k=5)
d = Counter(a=1, b=2)
print(c|d)