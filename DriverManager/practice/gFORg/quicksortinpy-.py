def partion (li, low, high):

    pivot = li[low]
    for i in range(low+1,high+1):
        print('i=',i)
        for j in range(high,low+1,-1):
            print('j=',j)
            if i>j :
             temp = li[j]
             li[j] = pivot
             li[low] = temp
             print('here')
             return (j)

            elif (li[i]>pivot and li[j]<pivot):
                temp = li[j]
                li[j] =li[i]
                li[i] = temp
                #print('swap')
                #print(li)
                break



def quick(li,low,high):
    s= partion(li,low,high)
    print(s)

    quick(li, low, s-1)
    print(li)
      #quick(li, s+1, high)



li = [5,3,1,9,8,2,4,7]
quick(li, 0, len(li)-1)
