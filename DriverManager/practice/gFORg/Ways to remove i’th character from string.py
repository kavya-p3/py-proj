def remIthchr(st,n):
    s1 = st[:n]
    s2 = st[n+1:]
    print(s1+s2)

s = input('enter sting ')
i = int(input('enter the ith value '))
remIthchr(s,i-1)
