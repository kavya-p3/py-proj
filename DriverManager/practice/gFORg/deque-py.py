from collections import deque

de = deque([1,3,6])
print(de)
de.append(7)
print('after appending',de)
de.pop()
print('after poping',de)
de.appendleft('k')
print('after appending left',de)
de.popleft()
print('after poping left',de)
print(de.index(3,0,2))
de.insert(2,66)
de.remove(6)
str = 'kavya'
de.extendleft(str)
de.extend(str)
de.reverse()
print(de)
de.rotate(2)
print(de)
print('len',len(de))
dt = deque(['r','i','m','a'])
d3= de.__imul__(3)
print('d3 is',d3)
print(maxlen(d3))
