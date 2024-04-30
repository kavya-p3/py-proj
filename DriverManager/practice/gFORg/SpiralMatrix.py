# arr = [[1,2,3,4],[12,13,14,5]]#,[11,16,15,6],[10,9,8,7]]
# l=0
# r=4
# t=0
# b=2
#
# while l<r and t<b :
#     for i in range(l,r):
#         print(arr[t][i])
#
#     t=t+1
#     for i in range(t,b):
#         print(arr[i][r-1])
#
#     r=r-1
#     for i in range(r-1,l-1,-1):
#         print(arr[b-1][i])
#
#     b=b-1
#     for i in range(b-1,t-1,-1):
#         print(arr[i][l])
#     l=l+1
#------------------------------------using recurrsion-----------------------------------------------
def  printMatrix(arr,t,b,l,r):
  if l<r and t<b :
    for i in range(l,r):
        print(arr[t][i])

    t=t+1
    for i in range(t,b):
        print(arr[i][r-1])

    r=r-1
    #if t < b:
    for i in range(r-1,l-1,-1):
            print(arr[b-1][i])

    b=b-1
    #if l < r:
    for i in range(b-1,t-1,-1):
            print(arr[i][l])
    l=l+1
    printMatrix(arr,t,b,l,r)



arr = [[1,2,3,4]]
l=0
r=4
t=0
b=1
printMatrix(arr,t,b,l,r)
