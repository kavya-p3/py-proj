def insertSort(arr):

    for i in range(1,len(arr)):
        current= arr[i]
        pos = i
        while pos >0 and arr[pos-1]>current:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = current




arr = [3, 44, 38, 5, 0]
insertSort(arr)