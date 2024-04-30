def revWords(s):
    lst = s.split(" ")
    print('the type is ',type(lst))
    s2 = ' '.join(lst)
    print('here is s2',s2)
    s1 = lst[::-1]
    f = ' '.join(str(x)for x in s1)
    print(f)


k = input('enter string of words ')
revWords(k)