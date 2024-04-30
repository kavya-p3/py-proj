di = {'a':0, 'b':800, 'c':900 , 100:'b'}
print(di)
k = int(input('enter the key to be removed '))

di.pop(k)

newDi = {k:v for k,v in di.items() if k!='a'}
kDi = {'abc':0, 'b':800, 'cd':900}
res = {**di,**kDi}
print('final',res)
str.count()

