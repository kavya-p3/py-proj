def selectSort(li,low, high):
 while low<high:
    p = li[low]
    #print(p)
    for i in range(low,high,1):
        #print('li[i]={},p={},i={}'.format(li[i],p,i))
        if li[i]<p:
            p=li[i]
            l=i
            #print('swap')


    li[low],li[l]=p,li[low]
    low+=1
    #print(li)



li = [89,45,68,90,29,34,17]
selectSort(li,0,len(li))
print(li)
