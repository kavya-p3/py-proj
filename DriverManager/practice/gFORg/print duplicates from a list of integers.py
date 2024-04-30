def printDup(lst):
    dup = []
    i = 0
    n = len(lst)
    for i in range(n):
        if lst[i] in lst[i+1:n]:
            if lst[i] not in dup:
             dup.append(lst[i])

    return dup

lst = [777,-1, 100, 0,100,-1,99,98,8,6000,0,100,555,777,99]
d = printDup(lst)
print(d)
