from collections import Counter

res=[]
arr=[3,0,1,0]
k=1
c=dict(Counter(arr))
print(c)
sorted(c.items(),key=lambda item: item[1],reverse=True)
print(c)

