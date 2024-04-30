from collections import *
st1 = 'kav ya'
st2 = 'aa   yvK'
c1=Counter(st1.lower())
c2=Counter(st2.lower())
print(c1)
print(c2)

for i in c2.keys():
    if i in c1.keys():
        if c1[i]!= c2[i]:
          print('cant be a per' )
    else:
        print('key not found in c1',i)







