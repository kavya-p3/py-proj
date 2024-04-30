# def stair(n):
#    res=[]
#    i=0
#    while i <=n:
#        if i==0 or i==1:
#            res.append(1)
#            i=i+1
#            continue
#
#        res.append(res[i-1]+res[i-2])
#        i=i+1
#    return res[n]
#
# print(stair(4))
# -----------------------------------------------------------

def recStair(n, res):
    print('r')
    if res[n]>0:
        return res[n]
    if n == 0:
        res[0] = 1
        return 1
    if n == 1:
        res[1] = 1
        return 1



    res[n] = recStair(n - 2, res) + recStair(n - 1, res)
    return res[n]


n=5
res=[0]*(n+1)
print((recStair(n,res)))
