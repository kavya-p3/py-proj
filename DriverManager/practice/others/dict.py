'''dict = {'name':'kp', 'id': 2000}
s=1,2,3
v=200
d2=dict.fromkeys(s,v)
y='name'

for i in dict:
    print(i)
    print(dict[i])
    print('key={},value={}'.format(i,dict[i]))'''

lst=[['k',1,0],['k2',8,0],['k3',0,9]]
d=dict(lst)
print(d)