def bbSort(li):
    l = len(li)
    for i in range(0,l-1):
        for j in range(0,l-1-i):
            #print('li[j]={},li[j+1]={},j={},i={}'.format(li[j],li[j+1],j,i))
            if li[j]>li[j+1]:
                print('swap')
                li[j+1],li[j]=li[j],li[j+1]



li = [70,60,50,40,30,20,10]
bbSort(li)
print(li)