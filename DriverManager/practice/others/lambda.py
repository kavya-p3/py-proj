from _functools import *

lst1 = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, lst1)
print(result)
