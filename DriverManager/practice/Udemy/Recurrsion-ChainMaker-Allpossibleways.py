def find_possible_ways(coins, target):

    arr = [[0 for j in range(target+1)] for i in range(len(coins)+1)]
    print(arr)

    for i in range(4):
           arr[i][0] = 'k'






    for i in arr:
        print(i)




target = 5
coins = [1, 2, 5]
find_possible_ways(coins,target)

# li=[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# print(li[2][4])
# for i in range(4):
#         for j in range(6):
#             if i == 1:
#                li[i][j]='k'
#
#             elif j == 0:
#                 li[i][j]='k'
#
# print(li)