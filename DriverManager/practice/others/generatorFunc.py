def mygen(x,y):
    while(x<y):
        yield x
        x+=1



print(next(mygen(1,8)))
print(next(mygen(1,8)))
print(next(mygen(1,8)))
print(next(mygen(1,8)))
print('lal lala lalalla')
for i in mygen(1,8):
    print(i)

