# def selSort(arr): #Ascending
#     j = 0
#     while j < len(arr):
#         minEl = arr[j]
#         k=j
#         for i in range(j,len(arr)):
#
#             if arr[i] < minEl:
#                 minEl = arr[i]
#                 k = i
#         arr[j], arr[k] = arr[k], arr[j]
#         j += 1
#     print(arr)

# def selSort(arr): #descending
#     j = 0
#     while j < len(arr):
#         minEl = arr[j]
#         k=j
#         for i in range(j,len(arr)):
#
#             if arr[i] > minEl:
#                 minEl = arr[i]
#                 k = i
#         arr[j], arr[k] = arr[k], arr[j]
#         j += 1
#     print(arr)


def selSort(arr): #descending
    j = 0
    while j < len(arr):
        minEl = j

        for i in range(j,len(arr)):

            if arr[i] < arr[minEl]:
                minEl = i

        arr[j], arr[minEl] = arr[minEl], arr[j]
        j += 1
    print(arr)


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
selSort(arr)
