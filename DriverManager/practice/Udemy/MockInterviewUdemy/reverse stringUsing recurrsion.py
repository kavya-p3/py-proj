
st = ''

def rev(s):
    if(len(s)==1):
        return s
    k = rev(s[1:])+s[0]
    return k


s='ABCD'
k=rev(s)
print(k)
