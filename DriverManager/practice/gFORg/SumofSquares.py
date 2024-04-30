def sumofSQ(n):
    sum = 0
    for i in range(n+1):
        sum+=i*i

    return sum

num = int(input('enter number '))
sum1 = sumofSQ(num)
print('sum is ',sum1)