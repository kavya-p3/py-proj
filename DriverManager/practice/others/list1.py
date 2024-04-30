lst = [10, 2, 3, 4, 5, -7, -2, 0]
tup=(1,6,99,100,88)
str='string'
max1 = 0
min1 = 0
n = len(lst)
i = 0

while i < n:
    if lst[i] > max1:
        max1 = lst[i]
    if lst[i] < min1:
        min1 = lst[i]
    i += 1

print('this is by kavya', max1, min1)
n1 = max(lst)
n2 = min(lst)
print('this is lst function for max', n1)
print('this is lst function for min', n2)
print(max(tup))
print(max(str))
lst.sort(reverse=True)
print(lst)
