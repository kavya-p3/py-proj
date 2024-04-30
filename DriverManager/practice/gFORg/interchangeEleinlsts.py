lst = [1,6,8,9,0,99,-2,-8]
print(lst)
x1,x2 = [int(z) for z in (input('enter 2 numbers ')).split(',')]
if x1 in lst and x2 in lst:
    i1 = lst.index(x1)
    i2 = lst.index(x2)
    lst[i2] = x1
    lst[i1] = x2
    print(lst)
else:
    print("ooopsy daisy either one or both elements is not in lst")


