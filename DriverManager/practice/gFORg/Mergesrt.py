def mergeSort(myList):


        if len(myList)==1:
            return myList
        mid = len(myList) // 2
        L=mergeSort(myList[:mid])
        R=mergeSort(myList[mid:])


        i=j=k=0
        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                myList[k] = L[i]
                i += 1
            else:
                myList[k] = R[j]

                j += 1
            k += 1

            # Checking if any element was left
        while i < len(L):
            myList[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            myList[k] = R[j]
            j += 1
            k += 1
        return myList



li= [-1,8,3,2,9,10,0]
mergeSort(li)
print("sorted",li)