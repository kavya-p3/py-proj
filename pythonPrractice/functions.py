def grocery (item='k',price=100.1):
    print('item= ', item)
    print('price= ', price)


print('enter  numbers separated by space')
lst = [int(x) for x in input().split()]
sum = 0
n = len(lst)
for i in lst:
    print (i)
    sum+=i
    avg=sum/n
print('sum= ',sum)
print('avg= ',avg)
