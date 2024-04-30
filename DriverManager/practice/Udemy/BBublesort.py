def bbsort(arr):
    j=1
    while j<len(arr):
      for i in range(len(arr)-j):
        if arr[i]> arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
      j+=1
      print(arr)
    print(arr)

arr = [3,50,8,38,5,47,0,13]
bbsort(arr)