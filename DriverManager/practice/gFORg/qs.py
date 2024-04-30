def partision (li, low, high):
    pivot = li[low]
    i = low
    for j in range(high-1,low,-1):
        print(li[j])
        if li[j]<pivot:
            i+=1
            li[i],li[j]=li[j],li[i]
            print(li)
        elif i>=j:
            li[j],li[low]=li[low],li[j]
            break
    print(li)


li = [5,3,1,9,8,2,4,7]
partision(li,0,len(li))




