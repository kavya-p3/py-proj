def allpermu(s):

    out=[]
    if len(s)==1:
        out=s

    for i,let in enumerate(s):
        #print('i={},let={}'.format(i,let))
        #print('s[:i]={}   s[i+1]={}'.format(s[:i],s[i+1:]))
        k=allpermu(s[:i] + s[i + 1:])
        print('k=',k)
        for perm in k:

            out+=[let+perm]
            print(out)

    return out

k=allpermu('abc')
print(k)

