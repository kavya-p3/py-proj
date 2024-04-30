arr= [12,11,15,3,10]
minst = arr[0]
profit = arr[1]-arr[0]

for prices in arr[1:]:

    minst = min(prices,minst)
    profit = max(profit, prices - minst)


print(profit)