from collections import *

odi = OrderedDict({'a': 2, 'b': 5, 'c': 999})
print(type(odi))
di = {'a': 2, 'b': 5, 'c': 999}
print(type(di))
odi.move_to_end('b',last=False)
print(odi.re)
