def countEorD(lst):
    ce = 0
    co = 0
    for i in lst:
        if i%2 == 0 :
            ce+=1
        else:
            co+=1
    return ce,co

lst = [1,9,0.5,5,2,881,101,-1,-99,9.6]
e,o = countEorD(lst)
print('even = {},odd={}'.format(e,o))