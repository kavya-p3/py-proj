def partision(li,low,high):
    pivot = li[low]

    for i in range(low+1,high):
        if li[i]>pivot:

            for j in range(high, low, -1):
                if i>j:
                    print(i,j)
                    temp = li[j]
                    # print(temp)
                    li[j] = li[low]
                    # print(li[low])
                    li[low] = temp
                    return j

                elif li[j] < pivot :
                    #print(li[i], li[j])
                    li[i], li[j] = li[j], li[i]
                    print('swap',i,j)
                    break


def quickS(li,low,high):

    if high>low:
      s = partision(li,low,high)
      quickS(li,low,s-1)
      quickS(li,s+1,high)




li = [5,3,1,9,8,2,4,7]
quickS(li,0,len(li)-1)
print(li)