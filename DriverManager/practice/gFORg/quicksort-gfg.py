def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        print('j={},arr[j]={}'.format(j,arr[j]))
        if arr[j] <= pivot:
            print('arr[j]={} is less thanpivot={}'.format(arr[j],pivot))
            # increment index of smaller element
            i = i + 1
            print('i=',i)
            print('a[i]={},a[j]={}'.format(arr[i],arr[j]))
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


li = [5,3,1,9,8,2,4,7]
quickSort(li, 0, len(li)-1)