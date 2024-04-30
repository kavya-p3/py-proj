d1 = {'k':0,'a':0}
d2 = {'k':5000,'a':90,'h':5,'k':3}
d1.update(d2)
print(d1.items())
d3=sorted(d1.items(),key=lambda x:x[0],reverse=True)
print(d3)