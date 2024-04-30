a=5
b=10
c=100
def glob():
   x=globals()['a']
   y=globals()['b']
   z = globals()['c']
   print(x,y,z)

glob()