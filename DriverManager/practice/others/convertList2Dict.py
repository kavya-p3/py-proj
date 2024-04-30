l1 = ['hawkins','Prestige','butterfly']
l2 = ['cooker','tawa','gasstove']

z = zip(l1,l2)
print(z)
d = dict(z)

for k,v in d.items():
    print('{:25s}--{:1s}ok'.format(k,v))