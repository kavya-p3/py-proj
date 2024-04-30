def countStr(s1,s2):
    l = []
    for i in s1:
        for j in s2:
            if i==j:
              if i not in l:
                  l.append(i)
                  break
    print(l)


s1,s2 = [str(s) for s in (input('enter 2 strings ')).split(' ')]
countStr(s1,s2)