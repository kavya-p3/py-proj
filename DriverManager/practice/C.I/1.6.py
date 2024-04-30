def compressString(st1):
    com = []
    i = 0
    while i < len(st1):
        c = 0
        for j in range(i, len(st1)):
            if st1[i] == st1[j]:
                c += 1
            else:
                break


        com.append(st1[i])
        com.append(c)
        i += c

    st = ''.join(str(s) for s in com)
    if len(st)> len(st1):
        print(st1)
    else:
      print(st)


st = 'aaccgg'
print(st)
compressString(st)
