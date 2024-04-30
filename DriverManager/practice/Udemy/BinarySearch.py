def binSearch(arr, el):
    if len(arr) > 0:

        mid = len(arr) // 2

        if el == arr[mid]:
            print('element found  ' )
            #return
        elif el > arr[mid]:
            binSearch(arr[mid + 1:], el)
        elif el < arr[mid]:
            binSearch(arr[:mid], el)

    else:
        print('element not found')
        return

# def binSearch(arr, el):
#    first = 0
#    last = len(arr)-1
#    flag= False
#
#    while first<= last:
#        mid = (first+last)//2
#        if arr[mid]== el:
#            flag = True
#            break
#        elif arr[mid]<el:
#            first= mid+1
#        else:
#            last=mid-1
#    if flag==False:
#        print('not found')
#    else:
#        print('found')



li = [10, 20, 30, 40, 50, 60, 70, 80]
binSearch(li, 50)
