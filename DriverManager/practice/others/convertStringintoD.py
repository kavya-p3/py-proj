str = "hawkins=cooker,prestige=tawa,butterfly=gasstove"
l1=[]

z=str.split(',')
for i in z:
     x=i.split("=")
     l1.append(x)

print(l1)
d=dict(l1)
print(d)

