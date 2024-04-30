def mergeSort(arr):
    if len(arr)==1:
        return arr
    else:
        n= len(arr)//2
        arrl = mergeSort(arr[0:n])
        arrr = mergeSort(arr[n:])

    i=0
    j=0
    k=0
    while i < len(arrl)and j<len(arrr):
        if arrl[i]>arrr[j]:
            arr[k]=arrr[j]
            j+=1
        else:
            arr[k]=arrl[i]
            i+=1
        k=k+1

        #checking any element is left
    while i <len(arrl):
            arr[k]=arrl[i]
            i+=1
            k=k+1
    while j < len(arrr):
            arr[k]=arrr[j]
            j+=1
            k+=1
    return arr

arr = [23, 29, 15, 19, 31,7, 9, 5]
arr1 = mergeSort(arr)
print(arr1)
