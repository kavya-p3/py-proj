s = 'KAV'
z = 'ab'
y = 99
v = 200
d1 = dict.fromkeys(s,v)
x=dict.fromkeys(z,y)
#print(d1.keys())
#print(d1.values())
#d2 = d1.get('A',0)
#print(d2)
print('before',d1)
d1.update()
d1.setdefault('a',-2)
d1.update({'l':-8})
print(d1)